import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': "kbjella-boto3-06022023", 'Key': "test_text_upload.txt"}, ExpiresIn=300)

print(response)