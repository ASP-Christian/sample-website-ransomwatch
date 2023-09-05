# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Install Firefox
RUN apt-get update && apt-get install -y firefox

# Copy the Firefox binary from the host to the container
COPY /usr/bin/firefox /usr/bin/firefox

# Set the executable permission for the Firefox binary
RUN chmod +x /usr/bin/firefox

# Copy the Python script into the container
COPY Groups/Qilin_Blog.py /app/Qilin_Blog.py

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run the Python script when the container launches
CMD ["python", "Qilin_Blog.py"]
