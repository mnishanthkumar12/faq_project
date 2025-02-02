# Use Python 3.10 or higher base image to avoid compatibility issues
FROM python:3.10

# Set working directory in the container
WORKDIR /app

# Copy all the project files into the working directory
COPY . /app

# Upgrade pip to the latest version to ensure smooth dependency installation
RUN pip install --upgrade pip

# Install project dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Django's development server
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
