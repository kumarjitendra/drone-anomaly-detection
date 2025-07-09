#!/bin/bash

# --- 0. Define paths and variables for your session ---
ML_MODEL_ROOT="ml_model"
INFERENCE_CODE_DIR="${ML_MODEL_ROOT}/inference_code"
MODEL_ARTIFACTS_DIR="${ML_MODEL_ROOT}/model_artifacts"
OUTPUT_TAR_PATH="model.tar.gz"
STAGING_DIR="temp_sagemaker_tar_staging"

# --- 1. Create the necessary source directories ---
echo "Creating source directories..."
mkdir -p "${INFERENCE_CODE_DIR}"
mkdir -p "${MODEL_ARTIFACTS_DIR}"

# --- 2. Create inference.py and requirements.txt ---
echo "Creating  content files..."

# NOTE: Replace this with your actual inference.py if needed
cat <<EOF > "${INFERENCE_CODE_DIR}/inference.py"
import json
import os

def model_fn(model_dir):
    import xgboost as xgb
    model_path = os.path.join(model_dir, "xgboost-model")
    booster = xgb.Booster()
    booster.load_model(model_path)
    return booster

def input_fn(request_body, request_content_type):
    import numpy as np
    import json
    if request_content_type == "application/json":
        data = json.loads(request_body)
        return np.array(data["instances"])
    raise Exception(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model):
    dmatrix = xgb.DMatrix(input_data)
    predictions = model.predict(dmatrix)
    return predictions.tolist()

def output_fn(prediction, accept):
    if accept == "application/json":
        return json.dumps({"predictions": prediction}), "application/json"
    raise Exception(f"Unsupported accept type: {accept}")
EOF

# Add minimal requirements (optional, add xgboost if needed)
echo "xgboost" > "${INFERENCE_CODE_DIR}/requirements.txt"

# --- 3. Ensure the trained model file exists ---
# IMPORTANT: Save model from Python using this line:
echo "Skipping model training - make sure 'xgboost-model' exists in ${MODEL_ARTIFACTS_DIR}"


# --- 4. Create the temporary staging directory ---
echo "Creating temporary staging directory: ${STAGING_DIR}..."
mkdir -p "${STAGING_DIR}/code"

# Copy files into staging
echo "Copying files to staging directory..."
cp -r "${INFERENCE_CODE_DIR}/." "${STAGING_DIR}/code/"
cp "${MODEL_ARTIFACTS_DIR}/xgboost-model" "${STAGING_DIR}/"

# --- 5. Display staging structure ---
echo -e "\nContents of staging directory (${STAGING_DIR}):"
ls -R "${STAGING_DIR}"

# --- 6. Create model.tar.gz archive ---
echo -e "\nCreating ${OUTPUT_TAR_PATH}..."
tar -czvf "${OUTPUT_TAR_PATH}" -C "${STAGING_DIR}" .

# --- 7. Verify contents ---
echo -e "\nContents of ${OUTPUT_TAR_PATH}:"
tar -tvf "${OUTPUT_TAR_PATH}"

# --- 8. Clean up ---
echo -e "\nCleaning up temporary staging directory..."
rm -rf "${STAGING_DIR}"

echo -e "\n✅ Packaging complete. You now have '${OUTPUT_TAR_PATH}' ready for SageMaker."
