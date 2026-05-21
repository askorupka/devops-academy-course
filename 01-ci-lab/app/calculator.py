def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def lambda_handler(event, context):
    a = event["a"]
    b = event["b"]

    operation = event["operation"]

    if operation == "add":
        result = add(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        return {"statusCode": 400, "body": "Unsupported operation"}

    return {
        "statusCode": 200,
        "body": result
    }
