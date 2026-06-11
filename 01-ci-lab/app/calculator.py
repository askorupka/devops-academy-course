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
        body = json.loads(event["body"]) if isinstance(event["body"], str) else event["body"]
    # Test from AWS console
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