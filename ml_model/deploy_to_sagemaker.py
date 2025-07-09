import sagemaker
import logging
from sagemaker.model import Model

# Initialize SageMaker session
print("🟢 Initializing SageMaker session...")
sagemaker_session = sagemaker.Session()

# Use your IAM role ARN explicitly (required when running outside SageMaker notebooks)
role_arn = "arn:aws:iam::285305988387:role/SageMakerExecutionRoleForDroneApp"
print(f"✅ role_arn: {role_arn}")
# Get the official public container URI for XGBoost
print("📦 Retrieving image URI...")
image_uri = sagemaker.image_uris.retrieve(
    framework="xgboost",
    region=sagemaker_session.boto_region_name,
    version="1.5-1"
)
print(f"✅ Image URI: {image_uri}")
# S3 path to your model artifact
model_data = "s3://jitendra-drone-raw-data/model-artifacts/model.tar.gz"
print(f"📁 Model artifact path: {model_data}")
# Create the model
print("🚀 Creating model...")
model = Model(
    image_uri=image_uri,
    model_data=model_data,
    role=role_arn,
    sagemaker_session=sagemaker_session
)

# Deploy the model to an endpoint
print("📡 Deploying model endpoint...")
predictor = model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large",
    endpoint_name="jitendra-drone-endpoint"
)

# Set logging level to suppress verbose output
logging.getLogger("sagemaker").setLevel(logging.WARNING)

print("✅ Model deployed successfully!")
