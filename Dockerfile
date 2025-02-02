# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Django runs on (default is 8000)
EXPOSE 8000

# Run the Django application with manage.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
