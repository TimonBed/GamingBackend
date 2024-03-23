# Use an official Python runtime as the base image
FROM python:3.11.4

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the container
COPY . .

# Expose the port your application listens on
EXPOSE 8000

# Define the command to run your application
CMD ["python", "manage.py", "runserver"]