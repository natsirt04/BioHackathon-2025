# Cervical Cancer Risk Prediction Project

## Overview

This project aims to predict the risk of cervical cancer using machine learning models and provide an interactive web application for users to assess their risk. It consists of:

- Data analysis and model development in a Jupyter Notebook
- A backend API for prediction
- A Streamlit frontend for user interaction

## Project Structure

```
BioHackathon-2025/
│
├── cervical_cancer.ipynb         # Data analysis and model development
├── cervical_cancer_csv.xlsx      # Dataset
├── requirements.txt              # Python dependencies
├── backend/
│   └── app.py                    # FastAPI backend for predictions
├── frontend/
│   └── main.py                   # Streamlit frontend web app
└── BioHackathon 2025 Opening Ceremony.pptx # Presentation
```

## How It Works

1. **Data Analysis** – The notebook (`cervical_cancer.ipynb`) performs exploratory data analysis and trains machine learning models to predict cervical cancer risk.
2. **Backend** – The FastAPI backend (`backend/app.py`) loads the trained model and exposes a `/predict` endpoint for risk prediction.
3. **Frontend** – The Streamlit app (`frontend/main.py`) provides a user-friendly interface for entering personal and medical information, then displays the predicted risk.

## Setup Instructions

1. **Build and Run with Docker Compose**

   ```
   docker compose up --build
   ```

2. **Access the App**
   - Frontend: Open your browser and go to `http://localhost:8501`
   - Backend: The API will be available at `http://localhost:8000`

This will automatically build the images and start both backend and frontend services.

## Files

- `cervical_cancer.ipynb`: Jupyter notebook for EDA and model training.
- `cervical_cancer_csv.xlsx`: Dataset used for analysis and modelling.
- `requirements.txt`: List of required Python packages.
- `backend/app.py`: FastAPI backend serving the prediction model.
- `frontend/main.py`: Streamlit web application for user input and displaying results.

## Technologies Used

- Python (pandas, scikit-learn, xgboost, seaborn, matplotlib, imbalanced-learn)
- FastAPI
- Streamlit
- Jupyter Notebook

## Authors

- Cadden Chua
- Tristan Ng
- Joanne Lee
- Meryl Yeo

## Licence

This project is for educational purposes. Please check dataset and code licences before public use.
