# Customer Churn Prediction App 🔮

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://telecom-churn-analyzer-3vzxnb2dtlh2kazf8eavr9.streamlit.app)

An interactive web application built with Streamlit to predict customer churn based on account information.

## 🚀 Live Demo

You can access the live application here: **[telecom-churn-analyzer.streamlit.app](https://telecom-churn-analyzer-3vzxnb2dtlh2kazf8eavr9.streamlit.app/)**

## 📖 Description

This project analyzes customer data to predict the likelihood of churn. An XGBoost classification model was trained on a telecom dataset and deployed as an interactive web app where users can input customer details to receive a real-time churn probability score.

## ✨ Key Features

- **Real-Time Prediction:** Get instant churn predictions based on user inputs.
- **Probability Score:** See the exact probability of a customer churning.
- **Interactive Interface:** Easy-to-use sliders and dropdowns for inputting customer data.

## 🛠️ Technologies Used

- **Python:** Core programming language.
- **Pandas:** Data manipulation and analysis.
- **Scikit-learn:** For machine learning pipelines and preprocessing.
- **XGBoost:** For the prediction model.
- **Streamlit:** To build and deploy the interactive web app.

## ⚙️ How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Romank12-vs/telecom-churn-analyzer.git](https://github.com/Romank12-vs/telecom-churn-analyzer.git)
    cd telecom-churn-analyzer
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
