import json


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def lambda_handler(event, context):
    body = json.loads(event["body"])

    a = body["a"]
    b = body["b"]
    operation = body["operation"]

    if operation == "add":
        result = add(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Unsupported operation"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"result": result})
    }
