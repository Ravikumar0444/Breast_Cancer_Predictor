# Breast Cancer Prediction using Machine Learning

## Overview

This project predicts whether a breast tumor is **Malignant** or **Benign** using Machine Learning techniques. The model is trained on breast cancer data and can assist in early diagnosis by analyzing medical features.

## Features

* Data preprocessing and cleaning
* Feature scaling
* Machine Learning model training
* Model evaluation using accuracy and classification metrics
* Prediction on new patient data

## Dataset

The dataset contains various medical measurements related to breast tumors.

Example features:

* Radius Mean
* Texture Mean
* Perimeter Mean
* Area Mean
* Smoothness Mean
* Compactness Mean
* Concavity Mean
* Symmetry Mean
* Fractal Dimension Mean

Target Variable:

* **M (Malignant)** → Cancerous tumor
* **B (Benign)** → Non-cancerous tumor

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook

## Project Structure

```text
Breast_Cancer_Predictor/
│
├── Breast_Cancer_Predictor.ipynb
├── data.csv
├── requirements.txt
├── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/ravikumar-0202/Breast_Cancer_Predictor.git
```

2. Navigate to the project folder

```bash
cd Breast_Cancer_Predictor
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

Open Jupyter Notebook:

```bash
jupyter notebook
```

Run:

```bash
Breast_Cancer_Predictor.ipynb
```

## Model Performance

Evaluation metrics may include:

* Accuracy Score
* Confusion Matrix

## Future Improvements

* Hyperparameter tuning
* Web application using Flask or Streamlit
* Deployment on Render or Railway
* Model explainability using SHAP

## Author

Ravi Ranjan

## License

This project is open-source and available under the MIT License.
