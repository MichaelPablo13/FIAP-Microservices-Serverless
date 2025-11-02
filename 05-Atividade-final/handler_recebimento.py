import json
import boto3
from botocore.exceptions import ClientError

sqs = boto3.client('sqs')
QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/839562665183/FeedbacksReclamacoesQueue'

def receive_feedback(event, context):
    """Função para receber feedbacks/reclamações via API Gateway."""
    try:
        body = json.loads(event["body"])

        # Enviar a mensagem para a fila SQS
        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(body)
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Feedback enviado com sucesso!"})
        }

    except ClientError as e:
        error_message = e.response['Error']['Message']
        error_code = e.response['Error']['Code']
        print(f"Erro ao enviar mensagem para a fila SQS: {error_message} ({error_code})")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": f"Erro ao processar solicitação: {error_message} ({error_code})",
                "queue_url": QUEUE_URL,
                "payload": event.get("body", {})
            })
        }

def handler(event, context):
    return receive_feedback(event, context)