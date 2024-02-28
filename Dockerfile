# FROM python:3.8-slim-buster

# RUN apt update -y && apt install awscli -y
# WORKDIR /app

# COPY . /app
# RUN pip install -r requirements.txt

# CMD ["python3","app.py"]

# Use the official Python 3.8 base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "app.py"]
