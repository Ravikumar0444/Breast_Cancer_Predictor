// ========================================
// 1. Define the 30 ML Model Features
// ========================================

const features = [
"radius_mean",
"texture_mean",
"perimeter_mean",
"area_mean",
"smoothness_mean",
"compactness_mean",
"concavity_mean",
"concave_points_mean",
"symmetry_mean",
"fractal_dimension_mean",
"radius_se",
"texture_se",
"perimeter_se",
"area_se",
"smoothness_se",
"compactness_se",
"concavity_se",
"concave_points_se",
"symmetry_se",
"fractal_dimension_se",
"radius_worst",
"texture_worst",
"perimeter_worst",
"area_worst",
"smoothness_worst",
"compactness_worst",
"concavity_worst",
"concave_points_worst",
"symmetry_worst",
"fractal_dimension_worst"
];

// ========================================
// 2. Generate the 30 Input Fields
// ========================================

const featuresContainer = document.getElementById("features-container");

features.forEach((feature) => {

const field = document.createElement("div");
field.className = "feature-field";

const label = document.createElement("label");
label.htmlFor = feature;

// Make the field name easier to read
label.textContent = feature
    .replaceAll("_", " ")
    .replace(/\b\w/g, letter => letter.toUpperCase());

const input = document.createElement("input");
input.type = "number";
input.id = feature;
input.name = feature;
input.step = "any";
input.required = true;
input.placeholder = "Enter " + label.textContent.toLowerCase();

// All inputs represent numerical measurements.
// Negative measurements are not allowed.
input.min = "0";

field.appendChild(label);
field.appendChild(input);

featuresContainer.appendChild(field);

});

// ========================================
// 3. Get the Form Elements
// ========================================

const predictionForm = document.getElementById("prediction-form");
const predictButton = document.getElementById("predict-button");
const resultContainer = document.getElementById("result-container");
const predictionResult = document.getElementById("prediction-result");
const predictionMessage = document.getElementById("prediction-message");

// ========================================
// 4. Send Input to FastAPI
// ========================================

predictionForm.addEventListener("submit", async (event) => {

// Prevent the browser from refreshing the page
event.preventDefault();

// Collect the 30 input values in the expected feature order
const inputData = {};

for (const feature of features) {

    const input = document.getElementById(feature);
    const value = input.valueAsNumber;

    if (!Number.isFinite(value) || value < 0) {
        alert("Please enter a valid, non-negative value for every feature.");
        input.focus();
        return;
    }

    inputData[feature] = value;
}

// Show a loading state
predictButton.disabled = true;
predictButton.textContent = "Analyzing...";
resultContainer.hidden = true;

try {

    // Call the FastAPI prediction endpoint
    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(inputData)
    });

    const result = await response.json();

    // Handle an unsuccessful API response
    if (!response.ok) {
        throw new Error(
            result.detail
                ? JSON.stringify(result.detail)
                : "The prediction request failed."
        );
    }

    // Display the prediction returned by FastAPI
    predictionResult.textContent = result.prediction;
    predictionMessage.textContent = result.message;

    resultContainer.hidden = false;

    // Bring the result into view
    resultContainer.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });

} catch (error) {

    console.error("Prediction error:", error);

    predictionResult.textContent = "Unable to predict";
    predictionMessage.textContent =
        "Could not connect to the prediction API. Make sure your FastAPI server is running.";

    resultContainer.hidden = false;

} finally {

    // Restore the button
    predictButton.disabled = false;
    predictButton.textContent = "Predict Classification";

}

});