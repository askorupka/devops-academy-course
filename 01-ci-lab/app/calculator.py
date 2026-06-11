import json


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def lambda_handler(event, context):
    # Function URL / API Gateway
    if "body" in event:
        if isinstance(event["body"], str):
            body = json.loads(event["body"])
        else:
            body = event["body"]
    # Test from AWS Console
    else:
        body = event

    a = float(body["a"])
    b = float(body["b"])
    operation = body["operation"]

    if operation == "add":
        result = add(a, b)
    elif operation == "divide":
        result = divide(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Unsupported operation"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"result": result})
    }
