import boto3
# Cliente em Low Level
s3api = boto3.client("s3", region_name="us-east-1")
bucket_name = "waltercoan1980"

s3api.create_bucket(Bucket = bucket_name)
print("bucket criado com sucesso...")
