import boto3

bucket_name = "waltercoan1980"
# API high level
s3 = boto3.resource('s3')

bucket = s3.Bucket(bucket_name)

for obj in bucket.objects.all():
    print(f"{obj.key} - Tamanho: {obj.size}")
