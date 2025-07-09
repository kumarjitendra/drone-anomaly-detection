 # General overview of the ML module
 /ml_model
│   ├── /training            # Jupyter notebooks, training scripts, data preparation
│   │   ├── train.py
│   │   └── EDA_notebook.ipynb
│   │
│   ├── /inference_code      # Contains inference.py and its direct dependencies
│   │   ├── inference.py     # Your SageMaker inference script
│   │   └── requirements.txt # Python dependencies for inference
│   │
│   ├── /model_artifacts     # (Optional) Raw, untarred model files if needed for versioning/review
│   │   └── trained_yolov5.pt
│   │
│   └── build_inference_tar.sh # Script to create model.tar.gz from inference_code and model_artifacts


## Documentation

- [How to Create Tar File](READEME_tar.md)
- [Deploy to SageMaker](README_sagemaker_deployment.md)


