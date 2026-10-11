Breast Cancer Predictor

A machine-learning web application that predicts a benign or malignant classification from 30 numerical features derived from breast cell measurements. The project uses a trained Logistic Regression model, StandardScaler, a FastAPI backend, and an HTML/CSS/JavaScript frontend.

Important medical disclaimer: This project is for educational and demonstration purposes only. It is not a medical device and must not be used to diagnose, screen for, or make treatment decisions about cancer. Predictions may be wrong. Always consult a qualified healthcare professional for medical advice.

Features

Web form for entering the 30 numerical features expected by the model

FastAPI REST endpoint for predictions

Feature scaling using the saved StandardScaler

Trained Logistic Regression model loaded from pickle files

Prediction result displayed in the frontend

Health-check endpoint to confirm that the model and scaler loaded

Tech Stack

Machine learning: Python, scikit-learn, Logistic Regression, StandardScaler

Backend: FastAPI, Uvicorn

Frontend: HTML, CSS, JavaScript

Saved artifacts: breast_cancer_model.pkl, scaler.pkl

Project Structure

Breast_Cancer_Predictor/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── Breast_Cancer_Prediction.ipynb
├── data.csv
├── breast_cancer_model.pkl
├── scaler.pkl
└── README.md

Your actual folder may contain additional files, such as a virtual environment. Do not commit a virtual environment to GitHub.

Requirements

Python 3.10 or a compatible Python version supported by the installed dependencies

pip

A modern web browser

VS Code is optional but useful

Run Locally

1. Clone the repository

git clone https://github.com/Ravikumar0444/Breast_Cancer_Predictor.git
cd Breast_Cancer_Predictor

2. Create and activate a virtual environment

Windows PowerShell:

python -m venv venv
.\venv\Scripts\Activate.ps1

If PowerShell blocks activation, you can use Command Prompt instead:

venv\Scripts\activate.bat

3. Install backend dependencies

python -m pip install --upgrade pip
pip install -r backend/requirements.txt

The backend requirements should include at least:

fastapi
uvicorn
scikit-learn
numpy

Use the same compatible scikit-learn version that was used to train and save the model and scaler. Pickle artifacts can fail to load across incompatible library versions.

4. Start the FastAPI backend

Run this command from the project root (the folder containing backend and the .pkl files):

python -m uvicorn backend.main:app --reload

The API should be available at:

Home: http://127.0.0.1:8000/

Health check: http://127.0.0.1:8000/health

Interactive API docs: http://127.0.0.1:8000/docs

The health check should report that the model and scaler are loaded.

5. Start the frontend

Keep the backend terminal running.

Open frontend/index.html with a local development server, such as the Live Server extension in VS Code. Do not open the page directly with a file:/// URL.

For the current frontend configuration, Live Server commonly uses:

http://127.0.0.1:5500

If Live Server uses a different address or port, update the allowed origins in the CORS configuration in backend/main.py to match the frontend origin. The frontend JavaScript currently sends prediction requests to:

http://127.0.0.1:8000/predict

Keep the API URL and CORS settings aligned with your local setup.

Prediction API

Endpoint

POST /predict
Content-Type: application/json

The request body must include all 30 numerical features in the exact names and order expected by the backend. The feature names are:

radius_mean
texture_mean
perimeter_mean
area_mean
smoothness_mean
compactness_mean
concavity_mean
concave_points_mean
symmetry_mean
fractal_dimension_mean
radius_se
texture_se
perimeter_se
area_se
smoothness_se
compactness_se
concavity_se
concave_points_se
symmetry_se
fractal_dimension_se
radius_worst
texture_worst
perimeter_worst
area_worst
smoothness_worst
compactness_worst
concavity_worst
concave_points_worst
symmetry_worst
fractal_dimension_worst

The API response contains the predicted classification and a message. The exact response format is defined in backend/main.py.

Example request

This example is for testing request formatting only. These values are illustrative, are not a validated clinical sample, and must not be interpreted as a medical result.

{
  "radius_mean": 14.0,
  "texture_mean": 20.0,
  "perimeter_mean": 90.0,
  "area_mean": 600.0,
  "smoothness_mean": 0.1,
  "compactness_mean": 0.1,
  "concavity_mean": 0.1,
  "concave_points_mean": 0.05,
  "symmetry_mean": 0.2,
  "fractal_dimension_mean": 0.06,
  "radius_se": 0.3,
  "texture_se": 1.0,
  "perimeter_se": 2.0,
  "area_se": 20.0,
  "smoothness_se": 0.005,
  "compactness_se": 0.02,
  "concavity_se": 0.03,
  "concave_points_se": 0.01,
  "symmetry_se": 0.02,
  "fractal_dimension_se": 0.003,
  "radius_worst": 16.0,
  "texture_worst": 25.0,
  "perimeter_worst": 105.0,
  "area_worst": 800.0,
  "smoothness_worst": 0.13,
  "compactness_worst": 0.2,
  "concavity_worst": 0.2,
  "concave_points_worst": 0.08,
  "symmetry_worst": 0.3,
  "fractal_dimension_worst": 0.07
}

You can test the API interactively at http://127.0.0.1:8000/docs while the backend is running.

Model Workflow

The user enters 30 numerical measurements in the frontend.

JavaScript validates the fields and sends them to the FastAPI backend as JSON.

The backend arranges the values in the feature order used during training.

The saved scaler transforms the features.

The trained Logistic Regression model predicts a class.

The frontend displays the returned classification.

The saved model and scaler must match the preprocessing and feature order used to train them. The notebook is included to document the model-training workflow.

Troubleshooting

Unable to predict / Failed to fetch: Confirm the backend is running at http://127.0.0.1:8000, then check the browser Console.

CORS error: Confirm the frontend origin (including hostname and port) is listed in allow_origins in backend/main.py.

Model or scaler not loaded: Run Uvicorn from the project root and confirm both .pkl files exist at the paths expected by backend/main.py.

HTTP 422: Check that all 30 required feature fields are included and have valid numeric values.

Pickle/scikit-learn compatibility error: Install a compatible scikit-learn version matching the environment used to save the artifacts.

Responsible Use and Limitations

This project demonstrates an ML deployment workflow; it is not validated for clinical use.

Do not enter identifiable patient information or use this app for real-world medical decisions.

A prediction is not a diagnosis, and no performance metric should be claimed unless it is measured and documented using a clearly described evaluation procedure.

If publishing the project, include the dataset's original source and license/usage terms, and ensure you have permission to redistribute data.csv and the serialized model files.

Future Improvements

Add automated tests for input validation and API responses

Report measured test-set metrics and a confusion matrix in the notebook

Improve frontend accessibility and form usability

Add deployment configuration and environment-based API URLs

Add model/version metadata and dependency version pinning

Author

Ravi Ranjan Kumar Ray

License

