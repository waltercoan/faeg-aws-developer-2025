from dotenv import load_dotenv
import boto3

load_dotenv()
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('cliente')
res = table.update_item(
    Key = {
        'id': 20
    },
    UpdateExpression = 'SET nome = :val1',
    ExpressionAttributeValues = {
        ':val1' : 'Zezinho da Silva'
    }
)
print(res)