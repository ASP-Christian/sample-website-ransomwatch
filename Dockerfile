# Use an Ubuntu-based image as the base image
FROM ubuntu:latest

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    firefox \
    tor

# Install Python dependencies from requirements.txt
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

# Set environment variables for TOR proxy
ENV TOR_PROXY socks5://127.0.0.1:9150

# Copy your Python scripts and other files into the container
COPY . /app

# This is the default entry point; you can override it in GitHub Actions
CMD ["python3", "Qilin_Blog.py"]
