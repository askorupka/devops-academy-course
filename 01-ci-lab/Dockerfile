FROM public.ecr.aws/lambda/python:3.12.2026.08.20.12

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/calculator.py ${LAMBDA_TASK_ROOT}/lambda_function.py

CMD ["lambda_function.lambda_handler"] 
