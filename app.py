import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

# ===================================
# PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Student Success Predictor",
    layout="wide"
)

# ===================================
# LOAD MODEL & ASSETS
# ===================================
@st.cache_resource
def load_resources():
    required_files = ["best_model.pkl", "scaler.pkl", "encoder.pkl", "data/data_fix.csv"]

    for file in required_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"File not found: {file}")

    model = joblib.load("best_model.pkl")
    scaler = joblib.load("scaler.pkl")
    encoder = joblib.load("encoder.pkl")

    df_sample = pd.read_csv("data/data_fix.csv")

    if "Status" in df_sample.columns:
        df_sample = df_sample.drop(columns=["Status"])

    feature_columns = df_sample.columns.tolist()

    return model, scaler, encoder, feature_columns


try:
    model, scaler, encoder, feature_columns = load_resources()
except Exception as e:
    st.error(f"Failed to load model/data files: {e}")
    st.stop()

# ===================================
# UI - HEADER
# ===================================
st.title("🎓 Student Academic Status Predictor")
st.markdown(
    "This application uses Machine Learning to predict whether a student will "
    "**Dropout** or **Graduate**."
)
st.divider()

# ===================================
# SIDEBAR INPUT
# ===================================
st.sidebar.header("📝 Student Data Input")

def get_user_inputs(columns):
    inputs = {}

    for col in columns:
        col_lower = col.lower()

        if "grade" in col_lower or "rate" in col_lower or "gdp" in col_lower:
            inputs[col] = st.sidebar.number_input(col, value=0.0, step=0.1)

        elif "age" in col_lower:
            inputs[col] = st.sidebar.slider(col, 15, 60, 20)

        elif "gender" in col_lower or "scholarship" in col_lower or "tuition" in col_lower:
            inputs[col] = st.sidebar.selectbox(
                col,
                [0, 1],
                help="0 = No/Female, 1 = Yes/Male"
            )

        else:
            inputs[col] = st.sidebar.number_input(col, value=0)

    return pd.DataFrame([inputs])


user_data = get_user_inputs(feature_columns)

# ===================================
# MAIN LAYOUT
# ===================================
col_input, col_space, col_result = st.columns([2, 0.2, 1.5])

with col_input:
    st.subheader("Entered Data")
    st.dataframe(
        user_data.T.rename(columns={0: "Value"}),
        height=450,
        width="stretch"
    )

with col_result:
    st.subheader("Prediction Result")

    if st.button("🚀 Check Student Status", width="stretch"):

        try:
            # Pastikan urutan kolom sesuai
            input_ordered = user_data[feature_columns]

            # Scaling
            scaled_array = scaler.transform(input_ordered)

            # Kembalikan jadi DataFrame supaya tidak warning
            scaled_input = pd.DataFrame(
                scaled_array,
                columns=feature_columns
            )

            prediction = model.predict(scaled_input)

            # Decode label
            if hasattr(encoder, "inverse_transform"):
                label = encoder.inverse_transform(prediction)[0]
            else:
                mapping = {0: "Dropout", 1: "Graduate"}
                label = mapping.get(prediction[0], prediction[0])

            st.divider()

            if label == "Graduate":
                st.success(f"### RESULT: {label}")
                st.info("The student is predicted to complete their studies successfully.")
                st.balloons()
            else:
                st.error(f"### RESULT: {label}")
                st.info("The student is at high risk of dropping out. Early intervention is recommended.")

            # ===================================
            # PROBABILITY SECTION
            # ===================================
            if hasattr(model, "predict_proba"):
                probs = model.predict_proba(scaled_input)[0]

                if hasattr(encoder, "classes_"):
                    classes = encoder.classes_
                else:
                    classes = ["Dropout", "Graduate"]

                max_prob = np.max(probs) * 100

                st.markdown(f"### 🎯 Confidence: **{max_prob:.2f}%**")

                prob_df = pd.DataFrame({
                    "Status": classes,
                    "Confidence (%)": probs * 100
                }).sort_values("Confidence (%)", ascending=False)

                st.write("### 📊 Model Confidence Details")
                st.dataframe(prob_df, width="stretch")

                st.bar_chart(
                    prob_df.set_index("Status"),
                    width="stretch"
                )

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

st.divider()
st.caption("Academic Status Prediction Dashboard v1.0 | Powered by Streamlit")