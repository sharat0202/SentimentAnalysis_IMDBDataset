# Use the official slim Python 3.8 image
FROM python:3.8-slim

# Copy the application files to the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install the required Python packages
RUN pip install -r requirements.txt

# Run the application
CMD ["python3", "app.py"]