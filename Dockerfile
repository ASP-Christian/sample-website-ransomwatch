# Use the official Python image as the base image
FROM python:3.8-slim

# Set environment variables
ENV TOR_PROXY="socks5://tor:9150"

# Install necessary dependencies
RUN pip install selenium pandas

# Copy your project files into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Run your script
CMD ["python", "Qilin.Blog.py"]
