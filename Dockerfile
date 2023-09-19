# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install Tor and Firefox in the container
RUN apt-get update && apt-get install -y tor firefox-esr

# Copy your Python script and requirements file to the container
COPY Groups/sample.py /app/sample.py
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the Tor Socks proxy port
EXPOSE 9150

# Start Tor service and run the Python script
CMD service tor start && python sample.py
