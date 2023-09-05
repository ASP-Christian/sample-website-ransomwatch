# Use an official Selenium with Python runtime
FROM selenium/standalone-python:3.8

# Set the working directory in the container
WORKDIR /app

# Install Firefox ESR
RUN apt-get update && apt-get install -y firefox-esr

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
