FROM python:3.11.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip first
RUN pip install --upgrade pip

# Copy requirements first for better caching
COPY requirements-railway.txt requirements.txt ./
RUN pip install --no-cache-dir -r requirements-railway.txt

# Copy application code
COPY . .

# Create static and templates directories if they don't exist
RUN mkdir -p static templates

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["sh", "-c", "python init_db.py 2>/dev/null || true && python bot.py"]