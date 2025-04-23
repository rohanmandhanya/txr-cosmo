# Use the official Playwright base image with Python
FROM mcr.microsoft.com/playwright/python:v1.43.0

# Set working directory
WORKDIR /app

# Install optional system packages (for Django + DB support)
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Install Playwright as a Python package
RUN pip install playwright

# Install Python dependencies for your project
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install Playwright browsers
RUN python -m playwright install

# Copy your Django project files
COPY . .

# Expose port (if running Django server)
EXPOSE 8000

# Default command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
