# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY app/ .

# Expose port
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]
