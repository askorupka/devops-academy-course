# base image: OS + libriaries preinstalled 
FROM python:3.12-slim

# set working directory - any operation will take place there
WORKDIR /app

# copy from my laptop to container (. = everything in current directory)
COPY . .

# install dependencies (this happens during build: is a one off operation)
RUN pip install --no-cache-dir -r requirements.txt 

# exposes the port
EXPOSE 5000

# runs the code in the container (in container: permanent process)
CMD ["python", "app.py"] 

# 1. build image (one template)
# 2. run container (living, many of them)
# difference between RUN and CMD
# difference between image and container