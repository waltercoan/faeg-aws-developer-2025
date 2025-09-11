import boto3
s3api = boto3.client("s3", region_name="us-east-1")
bucket_name = "waltercoan1980"

file_name = "./s3/index.html"
object_name = "index.html"

s3api.upload_file(file_name, bucket_name, object_name)
print("Arquivo enviado com sucesso para o S3")
