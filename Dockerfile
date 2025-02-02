# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose necessary ports
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
