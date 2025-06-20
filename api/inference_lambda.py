import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sm = boto3.client('sagemaker-runtime')

    bucket = event['queryStringParameters']['bucket']
    key = event['queryStringParameters']['key']

    obj = s3.get_object(Bucket=bucket, Key=key)
    img = obj['Body'].read()

    response = sm.invoke_endpoint(
        EndpointName='your-sagemaker-endpoint-name',
        ContentType='image/jpeg',
        Body=img
    )

    result = response['Body'].read().decode('utf-8')
    return {
        'statusCode': 200,
        'body': result
    }