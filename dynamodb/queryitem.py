from dotenv import load_dotenv
import boto3
from boto3.dynamodb.conditions import Key

load_dotenv()
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('cliente')

response = table.query(
    KeyConditionExpression = 
        Key('id').eq(2)
)

print(response)