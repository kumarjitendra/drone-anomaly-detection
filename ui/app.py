import streamlit as st
import requests
import boto3

st.title("🚁 Drone Image Anomaly Detection")

uploaded_file = st.file_uploader("Upload drone image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    s3 = boto3.client('s3')
    s3.upload_file("temp.jpg", "your-drone-raw", "test.jpg")

    st.image("temp.jpg", caption="Uploaded Drone Image")

    response = requests.get("https://<your-api-id>.execute-api.<region>.amazonaws.com/prod/predict",
                            params={"bucket": "your-drone-raw", "key": "test.jpg"})

    st.subheader("Detections")
    st.json(response.json())