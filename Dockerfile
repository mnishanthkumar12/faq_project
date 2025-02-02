# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Django's development server
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Run the app (replace this with your actual command)
CMD ["python", "app.py"]
