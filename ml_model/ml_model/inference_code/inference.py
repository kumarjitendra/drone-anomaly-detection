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
