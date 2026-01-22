# Use python 3.12 base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies (if needed for numpy/pandas/scikit-learn)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /root/.cache/pip

# Copy only necessary application files
COPY app/ ./app/
COPY model/ ./model/

# Remove __pycache__ directories
RUN find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true \
    && find . -type f -name "*.pyc" -delete

# Expose the application port
EXPOSE 8000

# Command to start FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]