# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY email_processor.py .

# Set environment variable for API key
ENV ANTHROPIC_API_KEY=""

# Run the application in demo mode by default
CMD ["python", "email_processor.py", "--demo"]
