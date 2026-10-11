from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import pickle
from pydantic import BaseModel, Field
import numpy as np

app = FastAPI(
    title="Breast Cancer Predictor API",
    description="API for predicting breast cancer using Machine Learning",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Locate the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths to the saved model and scaler
MODEL_PATH = BASE_DIR / "breast_cancer_model.pkl"
SCALER_PATH = BASE_DIR / "scaler.pkl"

# Load the trained model and scaler
with open(MODEL_PATH, "rb") as file:
    classifier = pickle.load(file)

with open(SCALER_PATH, "rb") as file:
    sc = pickle.load(file)


@app.get("/")
def home():
    return {
        "message": "Breast Cancer Predictor API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": True,
        "scaler_loaded": True
    }

# Define the 30 input features
class BreastCancerInput(BaseModel):
    radius_mean: float = Field(gt=0)
    texture_mean: float = Field(gt=0)
    perimeter_mean: float = Field(gt=0)
    area_mean: float = Field(gt=0)
    smoothness_mean: float = Field(gt=0)
    compactness_mean: float = Field(gt=0)
    concavity_mean: float = Field(ge=0)
    concave_points_mean: float = Field(ge=0)
    symmetry_mean: float = Field(gt=0)
    fractal_dimension_mean: float = Field(gt=0)

    radius_se: float = Field(ge=0)
    texture_se: float = Field(ge=0)
    perimeter_se: float = Field(ge=0)
    area_se: float = Field(ge=0)
    smoothness_se: float = Field(ge=0)
    compactness_se: float = Field(ge=0)
    concavity_se: float = Field(ge=0)
    concave_points_se: float = Field(ge=0)
    symmetry_se: float = Field(ge=0)
    fractal_dimension_se: float = Field(ge=0)

    radius_worst: float = Field(gt=0)
    texture_worst: float = Field(gt=0)
    perimeter_worst: float = Field(gt=0)
    area_worst: float = Field(gt=0)
    smoothness_worst: float = Field(gt=0)
    compactness_worst: float = Field(ge=0)
    concavity_worst: float = Field(ge=0)
    concave_points_worst: float = Field(ge=0)
    symmetry_worst: float = Field(gt=0)
    fractal_dimension_worst: float = Field(gt=0)


@app.post("/predict")
def predict_cancer(data: BreastCancerInput):

    # Arrange the features in the same order used during training
    features = np.array([[
        data.radius_mean,
        data.texture_mean,
        data.perimeter_mean,
        data.area_mean,
        data.smoothness_mean,
        data.compactness_mean,
        data.concavity_mean,
        data.concave_points_mean,
        data.symmetry_mean,
        data.fractal_dimension_mean,
        data.radius_se,
        data.texture_se,
        data.perimeter_se,
        data.area_se,
        data.smoothness_se,
        data.compactness_se,
        data.concavity_se,
        data.concave_points_se,
        data.symmetry_se,
        data.fractal_dimension_se,
        data.radius_worst,
        data.texture_worst,
        data.perimeter_worst,
        data.area_worst,
        data.smoothness_worst,
        data.compactness_worst,
        data.concavity_worst,
        data.concave_points_worst,
        data.symmetry_worst,
        data.fractal_dimension_worst
    ]])

    # Apply the same scaling used during training
    scaled_features = sc.transform(features)

    # Predict the diagnosis
    prediction = classifier.predict(scaled_features)[0]

    # Convert the prediction into a readable response
    if prediction == "M":
        diagnosis = "Malignant"
    else:
        diagnosis = "Benign"

    return {
        "prediction": diagnosis,
        "message": (
            "The model predicted malignant."
            if prediction == "M"
            else "The model predicted benign."
        ),
        "disclaimer": (
            "This is an educational ML prediction, not a medical diagnosis. "
            "Consult a qualified healthcare professional for medical advice."
        )
    }