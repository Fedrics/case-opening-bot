FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create static and templates directories if they don't exist
RUN mkdir -p static templates

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["python", "bot.py"]