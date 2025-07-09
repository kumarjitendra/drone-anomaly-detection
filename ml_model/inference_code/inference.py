import json
import os

# The model_fn function is called by SageMaker when the endpoint starts up.
# It's responsible for loading your trained model into memory.
# For a dummy model, we just return a placeholder.
def model_fn(model_dir):
    """
    Loads the model from the given model directory.
    For a dummy model, we don't actually load a real model, just return a placeholder.
    """
    print(f"Loading dummy model from: {model_dir}")
    # In a real model, you might have something like:
    # import torch
    # model = torch.load(os.path.join(model_dir, 'model.pt'))
    # model.eval()
    return "dummy_model_loaded_successfully"

# The input_fn function handles deserializing the incoming request.
# It converts the raw request body into a format your predict_fn can use.
def input_fn(request_body, request_content_type):
    """
    Deserializes the input request.
    Expected content type is 'image/jpeg' as per your Lambda, but for a dummy,
    we don't strictly parse it since predict_fn doesn't use the actual image.
    """
    print(f"Received input with content type: {request_content_type}")
    print(f"Request body length: {len(request_body)} bytes")
    # If it were a real image, you might parse it into a numpy array or PIL Image:
    # from PIL import Image
    # import io
    # return Image.open(io.BytesIO(request_body))
    return request_body # Just return the raw body for dummy purposes

# The predict_fn function performs the actual inference.
# It takes the deserialized input and the loaded model, and returns a prediction.
def predict_fn(input_object, model):
    """
    Performs dummy inference and returns hardcoded predictions.
    The 'input_object' and 'model' parameters are ignored for this dummy.
    """
    print(f"Performing dummy prediction.")
    print(f"Input object (ignored): {input_object}")
    print(f"Model placeholder (ignored): {model}")

    # This is the hardcoded JSON output you want
    predictions = {
        "predictions": [
            {"label": "car", "confidence": 0.93},
            {"label": "person", "confidence": 0.87}
        ]
    }
    return predictions

# The output_fn function serializes the prediction back into the response format.
# It converts your predict_fn's output into bytes that SageMaker returns to the client.
def output_fn(prediction, accept_content_type):
    """
    Serializes the prediction result into the expected response format.
    """
    print(f"Serializing output prediction: {prediction}")
    print(f"Accept content type: {accept_content_type}")

    if accept_content_type == "application/json":
        # Convert the Python dictionary 'prediction' into a JSON string, then encode to bytes.
        return json.dumps(prediction), accept_content_type
    else:
        raise Exception(f"Unsupported accept content type: {accept_content_type}")