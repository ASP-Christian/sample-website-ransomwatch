# Use an official Python runtime with Firefox and geckodriver
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y firefox-esr && pip install -r requirements.txt

# Copy the Python script into the container
COPY Groups/Qilin_Blog.py /app/Qilin_Blog.py

# Run the Python script when the container launches
CMD ["python", "Qilin_Blog.py"]
