
import boto3
import json

bedrock = boto3.client(service_name='bedrock-runtime')

def lambda_handler(event, context):

    print("boto3 version"+ boto3.__version__)
    print(event['text'])

    prompt="Generate a list of potential career paths for a history student. {}".format(event['text'])
    body = json.dumps({
        "prompt": prompt,
        "maxTokens": 1525,
        "temperature": 0.7,
        "topP": 1,
        "stopSequences":[],
        "countPenalty":{"scale":0},
        "presencePenalty":{"scale":0},
        "frequencyPenalty":{"scale":0}})
    modelId = 'ai21.j2-ultra-v1'
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())
    
    result = json.dumps(response_body.get("completions")[0].get("data").get("text"))
    print(result)

    return result


