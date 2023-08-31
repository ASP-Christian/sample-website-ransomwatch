# Use a base image with Python
FROM python:3.8-slim

# Install required dependencies
RUN apt-get update && \
    apt-get install -y tor firefox-esr wget && \
    wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz && \
    tar -C /usr/local/bin -xzvf /tmp/geckodriver.tar.gz && \
    chmod +x /usr/local/bin/geckodriver && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/geckodriver.tar.gz

# Copy your script and dependencies into the container
COPY Groups /app

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Start Tor service and your script when the container starts
CMD service tor start && python Qilin_Blog.py
