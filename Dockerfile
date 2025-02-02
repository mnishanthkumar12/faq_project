# Step 1: Use an official Python image from the Docker Hub
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Install system dependencies (e.g., for MySQL, PostgreSQL, etc. if needed)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy requirements file into the container
COPY requirements.txt /app/

# Step 5: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the Django project files into the container
COPY . /app/

# Step 7: Set environment variables
ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Step 8: Run Django management commands (migrate, collectstatic, etc.)
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

# Step 9: Expose the port Django will run on
EXPOSE 8000

# Step 10: Set the entrypoint to run the Django server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
