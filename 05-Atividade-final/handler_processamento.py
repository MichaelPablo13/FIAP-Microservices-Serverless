import boto3
# import uuid
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FeedbacksReclamacoes')

def inserir_feedback(id_cliente, descricao, categoria, data_hora):
    try:
        print({
                'id_cliente': id_cliente,
                'descricao': descricao,
                'categoria': categoria,
                'data_hora': data_hora
            })
            
        response = table.put_item(
            Item={
                'id_cliente': id_cliente,
                'descricao': descricao,
                'categoria': categoria,
                'data_hora': data_hora
            })
        
    except ClientError as e:
        print(f"Erro ao salvar no DynamoDB: {e}")
    except Exception as e:
        print(f"Erro geral: {e}")

    return response

def handler(event, context):
    print(json.dumps(event))
    print(event["Records"][0]["body"])
    for record in event["Records"]:
        body = json.loads(record["body"])
        response_dynamo = inserir_feedback(body["id_cliente"], body["descricao"], body["categoria"], body["data_hora"])
    response = {
        'statusCode': 200,
        'body': response_dynamo
    }

    return response
