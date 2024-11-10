# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements and application files
COPY . .

# Install the required system packages
RUN apt-get update && apt-get install -y libgl1 && rm -rf /var/lib/apt/lists/*

# Install the required Python packages
RUN pip install --no-cache-dir opencv-python flask

# Expose the port that Flask will run on
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "camera_feed.py"]
