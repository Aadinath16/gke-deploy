# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for security updates & pip build)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY app/ .

# Use non-root user for security
RUN useradd -m flaskuser
USER flaskuser

# Gunicorn startup command
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "app:app"]
