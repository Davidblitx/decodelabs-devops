# Base image - lightweight Python
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependencies first (layer caching best practice)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Document which port the app uses
EXPOSE 8080

# Command to run when container starts
CMD ["python", "app.py"]
