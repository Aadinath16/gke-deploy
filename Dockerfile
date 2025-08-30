# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies in one layer
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app

# Expose the port Flask/Gunicorn will run on
EXPOSE 8080

# Run Gunicorn (production-ready server)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--workers", "3", "--timeout", "120", "app:create_app()"]

