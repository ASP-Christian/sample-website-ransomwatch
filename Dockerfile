# Use a base image with Python, Tor, Firefox, and geckodriver
FROM python:3.8-slim

# Install Tor and Firefox
RUN apt-get update && \
    apt-get install -y tor firefox-esr && \
    apt-get clean

# Install geckodriver
RUN apt-get install -y wget && \
    wget -O /usr/local/bin/geckodriver https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64 && \
    chmod +x /usr/local/bin/geckodriver

# Copy your script and dependencies into the container
COPY Groups /app

# Set the working directory
WORKDIR /app

# Start your script when the container starts
CMD ["python", "Qilin_Blog.py"]
