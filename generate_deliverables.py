from pptx import Presentation
from pptx.util import Inches, Pt

report_md = """# Bank Customer Churn Prediction Report

## 1. Project Overview
This project builds a machine learning solution to predict whether a bank customer will churn (leave the bank), based on customer demographics and transaction features.

## 2. Problem Statement
Customer churn leads to revenue loss for banks. The goal is to identify at-risk customers and support proactive retention strategies.

## 3. Data and Features
- Source dataset includes customer details such as credit score, age, tenure, balance, number of products, country, gender, and churn outcome.
- Irrelevant columns were removed.
- Encoded categorical variables using one-hot encoding for gender and country.
- Created a derived feature: `balance_per_product` = balance / (products_number + 1).

## 4. Preprocessing
- Standard scaling of numerical features using `StandardScaler`.
- One-hot encoding for categorical fields: gender and country.
- Feature engineering improved model interpretability and prediction performance.

## 5. Model Architecture
- Used an ensemble Voting Classifier combining:
  - Support Vector Machine (SVM)
  - Gradient Boosting Classifier
  - XGBoost Classifier
- Voting method: soft voting based on predicted probabilities.

## 6. Application and Deployment
- Interactive Streamlit app available via `app.py`.
- User inputs customer profile data and receives churn prediction probability.
- The app includes real-time prediction feedback and risk insight.

## 7. Files Added
- `Bank_Churn_Presentation.pptx`: Project presentation slides.
- `project_report.md`: Detailed project report.

## 8. Next Steps
- Add additional features and model tuning.
- Incorporate more customer behavior data.
- Convert the report to PDF if needed.
"""

with open("project_report.md", "w", encoding="utf-8") as f:
    f.write(report_md)

prs = Presentation()

slides = [
    {
        "title": "Bank Customer Churn Prediction",
        "body": [
            "Machine learning solution to predict customer churn for a bank.",
            "Includes model training, deployment, and an interactive Streamlit app."
        ]
    },
    {
        "title": "Problem Statement",
        "body": [
            "Customer churn reduces bank revenue and increases acquisition costs.",
            "Predict churn early to enable retention interventions."
        ]
    },
    {
        "title": "Approach",
        "body": [
            "Data cleaning, categorical encoding, feature engineering.",
            "Created balance-per-product feature and scaled numerical inputs."
        ]
    },
    {
        "title": "Model",
        "body": [
            "Ensemble Voting Classifier with SVM, Gradient Boosting, and XGBoost.",
            "Soft voting uses predicted probabilities for final decision."
        ]
    },
    {
        "title": "Deployment",
        "body": [
            "Streamlit app in `app.py` for interactive churn prediction.",
            "User enters profile data and receives churn risk probability."
        ]
    },
    {
        "title": "Deliverables",
        "body": [
            "Report: `project_report.md`",
            "Presentation: `Bank_Churn_Presentation.pptx`"
        ]
    }
]

for slide_info in slides:
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    body_shape = slide.shapes.placeholders[1]
    title.text = slide_info["title"]
    text_frame = body_shape.text_frame
    text_frame.clear()
    for i, paragraph in enumerate(slide_info["body"]):
        if i == 0:
            p = text_frame.paragraphs[0]
            p.text = paragraph
        else:
            p = text_frame.add_paragraph()
            p.text = paragraph
            p.level = 0
            p.font.size = Pt(18)

prs.save("Bank_Churn_Presentation.pptx")

print("Created project_report.md and Bank_Churn_Presentation.pptx")
