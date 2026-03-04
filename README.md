# Jaya Jaya Institute Student Monitoring Dashboard

## Bussiness Understanding

Jaya Jaya Institute, a higher education institution established in 2000, is well known for the strong reputation of its graduates. However, the institution faces a serious challenge in the form of a high student drop out rate.

To address this issue, Jaya Jaya Institute seeks to identify students at risk of dropping out at an early stage, allowing for targeted interventions such as specialized guidance. Therefore, an analysis of student performance data is required, which will then be developed into an dashboard that serves as a monitoring tool and supports decision-making for the institution.

## Business Problems

- What is the total number of enrolled students, and what is their graduation rate?

- How do demographic characteristics, such as gender and age at enrollment, affect the proportion of students who successfully graduate or drop out at Jaya Jaya Institute?

- To what extent do scholarship status and timely tuition payment serve as distinguishing indicators in maintaining student retention rates?

- Which factors demonstrate the strongest predictive power in identifying students at high risk of dropping out during the early stages of their academic program?

## Project Scope

- **Preparation:** Setting up programming libraries and loading the `data.csv` dataset.

- **Data Understanding:** Examining data structure, identifying missing values, and exploratory data analysis (EDA).

- **Data Preparation / Preprocessing:** Transforming categorical variables through encoding, adjusting feature scales using scaling, and balancing class distribution with SMOTE. After preprocessing, the dataset is prepared for modeling by performing data splitting, where the features (X) are separated from the target variable (y).

- **Modeling:** Building predictive models that can identify students at risk of dropping out. 

- **Evaluation:** Testing model performance and identifying the most influential factors.

- **Visualization (Dashboard):** Developing a student monitoring dashboard with Looker Studio to track academic performance and drop out risk in real time. The project also integrates a Streamlit app, allowing users to upload new data and view predictions with dynamic visualizations.
  
- **Conclusion and Recommended Action Items:** Summarizing the final insights by identifying the most significant features influencing drop out prediction and selecting the most effective predictive model. This stage also involves formulating data-driven strategic interventions to address the identified drop out risks.

## Preparation

The following are the steps to set up the environment:

### Data Source  
https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance 

### Environment Setup

If you install Python using Anaconda or Miniconda, you can use Conda as both a package manager and environment management system. Below are the steps to create a virtual environment for running the prediction:

1. Open Terminal or PowerShell.
2. Run the following command to create a new virtual environment:

```
conda create --name student_monitoring python=3.12.12
```

3. Activate the virtual environment:

```
conda activate student_monitoring
```

4. Install all required libraries:

```
pip install -r requirements.txt
```

5. Launch Jupyter Notebook:

```
jupyter-notebook
```

6. Open the `app.py` file.

7. Running Streamlit locally for student monitoring:

```
streamlit run app.py
```

## Business Dashboard

The Jaya Jaya Institute Student Monitoring Dashboard is designed as a visual tool for the Academic and Student Affairs Department to track and analyze key indicators related to student performance and retention.

**Looker Studio Dashboard Link:**
https://lookerstudio.google.com/u/0/reporting/8997cdad-4cf5-42b4-b2fb-de1f95d27a68/page/8xRqF

## Running a Machine Learning System

The Ensemble Voting Classifier model has been developed to predict students at risk of dropping out, and it is deployed through a Streamlit Cloud web application accessible via the following link:
https://jaya-jaya-institute-student-monitoring-dashboard.streamlit.app/

```
pip install -r requirements.txt
```

```
streamlit run app.py
```

## Conclusion

- The feature `Curricular_units_2nd_sem_approved` has the highest importance (about 0.12). This means that passing classes at the end of the first year is the biggest sign of whether a student will stay.

- Features like `Tuition_fees_up_to_date` and `Scholarship_holder` show that students who struggle to pay or lose their scholarships are at a much higher risk of drop out.

- Other factors like `Gender`, `Age_at_enrollment`, and being `Displaced`. While these factors are not as strong as grades, they are still important. They help the institute identify students who might struggle to adapt or who need extra support in a new environment.

From the evaluation of multiple models, the Ensemble Voting Classifier is the best-performing model for this monitoring system, achieving a top accuracy of 91.6% and an outstanding ROC-AUC score of 0.958. By combining the strengths of multiple algorithms, it provides the most robust and stable predictions, particularly in accurately distinguishing between students who will stay and those at risk of dropping out. While XGBoost and Random Forest are strong contenders, the Ensemble Voting Classifier balance of precision and recall makes it the primary choice for effective early intervention.

## Recommended Action Items

- Since `Curricular_units_2nd_sem_approved` is the most critical factor, the institute should identify struggling students early. If a student fails many classes in their first semester, they should be required to join a tutoring or mentoring program immediately. This helps them stay on track and prevents them from losing the momentum needed to finish their first year successfully.

- Because `Tuition_fees_up_to_date` is a major factor, the finance office should work closely with counselors. When a student stops paying, the institute should check if they are having money problems. For those who lose their scholarship `(Scholarship_holder)`, the institute could offer emergency grants or part-time campus jobs so they don't have to drop out due to costs.

- The data shows that a student’s age `(Age_at_enrollment)` and whether they moved from another city `(Displaced)` affect their risk. The institute should create special orientation programs or support groups for older students and those living away from home. These students often face more stress, so providing them with a community or affordable housing can help them feel more comfortable and avoid a drop out.
