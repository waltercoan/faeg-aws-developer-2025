from dotenv import load_dotenv
import boto3
from boto3.dynamodb.conditions import  Attr

load_dotenv()
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('cliente')

res = table.scan(
    FilterExpression = Attr('id').eq('Zezinho da Silva')
)
print(res)