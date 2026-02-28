# Jaya Jaya Institute Student Monitoring Dashboard

## Bussiness Understanding

Jaya Jaya Institute, a higher education institution established in 2000, is well known for the strong reputation of its graduates. However, the institution faces a serious challenge in the form of a high student dropout rate.

To address this issue, Jaya Jaya Institute seeks to identify students at risk of dropping out at an early stage, allowing for targeted interventions such as specialized guidance. Therefore, an analysis of student performance data is required, which will then be developed into an dashboard that serves as a monitoring tool and supports decision-making for the institution.

## Business Problems

Jaya Jaya Institute faces the problem of high student dropout rates, which can damage the reputation and performance of the institution. The main issue is the lack of a system capable of identifying students at risk of dropping out at an early stage. Therefore, data analysis and monitoring dashboards are needed to help the institution detect dropout risks earlier, provide appropriate guidance, and support data-driven decision making to reduce dropout rates.

## Project Scope

- **Preparation:** Setting up programming libraries and loading the `data.csv` dataset.

- **Data Understanding:** Examining data structure, identifying missing values, and exploratory data analysis (EDA).

- **Data Preparation / Preprocessing:** Transforming categorical variables through encoding, adjusting feature scales using scaling, and balancing class distribution with SMOTE. After preprocessing, the dataset is prepared for modeling by performing data splitting, where the features (X) are separated from the target variable (y).

- **Modeling:** Building predictive models that can identify students at risk of dropping out. 

- **Evaluation:** Testing model performance and identifying the most influential factors.

- **Visualization (Dashboard):** Developing a student monitoring dashboard with Looker Studio to track academic performance and dropout risk in real time. The project also integrates a Streamlit app, allowing users to upload new data and view predictions with dynamic visualizations.
  
- **Conclusion and Recommended Action Items:** Summarizing the overall findings of the analysis, including identifying the most significant factors influencing student dropout and selecting the best-performing predictive model, as well as providing strategic recommendations for intervention programs.

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

This project successfully identified the key factors influencing student dropout risk at Jaya Jaya Institute. Correlation analysis revealed ten major factors most strongly associated with the likelihood of students dropping out. These correlations illustrate both the strength and direction of the relationship between each variable and student status (dropout). Variables with higher correlation values have a more significant impact on dropout risk.

Based on the results, the factors include: **Age at enrollment**, **Debtor**, **Gender**, **Application mode**, **Marital status**, **Curricular units without evaluations (semester 1 & 2)**, **Mother’s qualification**, **Previous qualification**, and **Inflation rate**. For instance, students who are older at the time of enrollment or those with debtor status tend to be at higher risk of dropping out. Meanwhile, academic factors such as the number of curricular units without evaluations also show a strong relationship with study success.

From the evaluation of multiple models, the **Ensemble Voting Classifier** emerged as the most robust and stable performer, achieving the highest accuracy (91.6%) and the best ROC-AUC score (0.958), which highlights its strong ability to discriminate between classes. Both **XGBoost** and **Random Forest** delivered competitive results with accuracies around 91% and ROC-AUC scores above 0.95, though their recall for the Dropout class was slightly lower. In comparison, **SVM** remained solid but lagged behind with an accuracy of 89.8% and a ROC-AUC of 0.94. Overall, **Ensemble Voting Classifier** stands out as the primary choice for the monitoring system, with **XGBoost** serving as a strong baseline benchmark and **Random Forest** offering a more interpretable alternative.

## Recommended Action Items

Based on the findings, Jaya Jaya Institute should apply targeted actions that focus on the main factors influencing student dropout. Students who enroll at an older age should receive personal academic guidance and flexible learning options to support their needs. Financial support programs should be improved, especially for students with debtor status, by providing better scholarship options, payment installment plans, and early financial monitoring to prevent dropouts caused by financial problems.

The institute should also provide inclusive and gender-sensitive support services, and adjust retention strategies based on students’ application mode and marital status. Early academic monitoring is very important for students who have many curricular units without evaluations, as this may show low participation or academic difficulties that require quick support such as tutoring or mentoring. In addition, mentoring and academic bridging programs should be offered to students whose parental education background or previous qualifications may affect their academic preparation.

Finally, the institution should consider external economic factors such as inflation when creating financial policies and should regularly retrain and evaluate the predictive model to maintain long-term accuracy and effectiveness in reducing student dropout rates.
