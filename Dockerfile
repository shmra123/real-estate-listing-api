# Use the official Python image as a base
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app
ENV FLASK_APP=real_estate_listing_api


# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 5000
ENV MONGO_DB_URI=mongodb://host.docker.internal:27017/realestate


# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

