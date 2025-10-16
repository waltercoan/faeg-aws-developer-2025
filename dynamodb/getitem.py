from dotenv import load_dotenv
import boto3

load_dotenv()
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('cliente')

res = table.get_item(
    Key = { 
        'id': 20
    }
)

item = res['Item']
print(item)