import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    bucket_name = event['bucket_name']
    file_name = event['file_name']
    file_content = event['file_content']  
    

    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=file_content
    )
    

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'File {file_name} uploaded to {bucket_name}'
        })
    }