
## Documentation
[Script to create model.tar.gz from inference_code and model_artifacts]build_inference_tar.sh

#---0. Run  build_inference_tar script to build tar file---
sh build_inference_tar.sh

# Best practices for "model.tar.gz" creation
Do not include the README file in model.tar.gz. The README is meant for human reference, not for use by the SageMaker endpoint at runtime. Including it unnecessarily increases the file size, leading to longer download times and potential unexpected behavior during deployment.
 
#---1. Upload this tar file to S3 bucket (jitendra-drone-raw-data) ---
aws s3 cp model.tar.gz s3://jitendra-drone-raw-data/model-artifacts/model.tar.gz

#---2. How to delete tar file on S3 bucket(jitendra-drone-raw-data) if you wish to do so ---
 ##Using AWS CLI 
 
aws s3 rm s3://jitendra-drone-raw-data/model.tar.gz







 