import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='kbjella-boto3-06022023'
)

print(response)