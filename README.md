# 🚁 Drone-based Anomaly Detection (AWS MVP)

This project demonstrates a minimal end-to-end machine learning pipeline for anomaly detection on drone-captured imagery, using AWS cloud-native services.

---

## 📦 Folder Structure

```
├── infrastructure/   # IaC (CloudFormation/CDK)
├── ml_model/         # Notebooks and model training/deployment
├── api/              # Lambda functions and API Gateway handlers
├── ui/               # Streamlit UI or mobile front-end
└── README.md         # Overview and instructions
```

---

## 🛠️ Tech Stack

- **AWS S3**: Image storage
- **AWS Lambda**: API logic
- **API Gateway**: REST interface
- **Amazon SageMaker**: ML inference (YOLOv5 or custom anomaly model)
- **Streamlit**: Frontend UI

---

## 🚀 Quick Start

### 1. Set up AWS resources
- Create an S3 bucket: `your-drone-raw`
- Deploy your SageMaker endpoint (e.g., YOLOv5)

### 2. Deploy Lambda
Edit and deploy `api/inference_lambda.py` with access to:
- `s3:GetObject`
- `sagemaker:InvokeEndpoint`

### 3. Launch the Streamlit UI
Update `ui/app.py` with:
- Your API Gateway endpoint URL
- Your S3 bucket name

Then run:
```bash
streamlit run ui/app.py
```

---

## 🧠 Ideas for Future Expansion

- Use S3 event triggers instead of API Gateway
- Integrate DynamoDB for result storage
- Add multi-class anomaly detection
- Extend UI with map-based views or mobile app

---

## 📬 Contact
Built by [Your Name] · AI Product Owner · AWS Certified

---