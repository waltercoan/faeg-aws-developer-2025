from dotenv import load_dotenv
import boto3

load_dotenv()
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('cliente')
response = table.put_item(
    Item={
        'id': 2,
        'nome': 'Luizinho',
        #'idade': 30,
        #'email': '',
        #'telefone': '1234-5678'
    }
)
print("Item inserted successfully:", response)