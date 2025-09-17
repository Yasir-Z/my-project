# Use official Python runtime as a base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files into the container
COPY . .

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

