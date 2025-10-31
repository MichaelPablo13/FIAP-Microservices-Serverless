# import json
# import boto3
# import os

# sqs = boto3.client('sqs')
# QUEUE_URL = os.environ.get('FEEDBACK_QUEUE_URL', 'https://sqs.us-east-1.amazonaws.com/123456789012/FeedbacksReclamacoesQueue')

# def receber_feedback(event, context):
#     body = json.loads(event['body'])
#     response = sqs.send_message(
#         QueueUrl=QUEUE_URL,
#         MessageBody=json.dumps(body)
#     )
#     return {
#         "statusCode": 200,
#         "body": json.dumps({"message": "Feedback recebido com sucesso."})
#     }
