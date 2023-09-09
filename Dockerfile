# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Install Tor and Firefox
RUN apt-get update && apt-get install -y tor firefox-esr

# Start Tor as a background service when the container is launched
CMD ["tor"]

# Download and install Geckodriver
RUN apt-get install -y wget && \
    wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz && \
    tar -xvzf geckodriver-v0.33.0-linux64.tar.gz && \
    chmod +x geckodriver && \
    mv geckodriver /usr/local/bin/ && \
    rm geckodriver-v0.33.0-linux64.tar.gz

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the script into the container at /app
COPY Groups/Qilin_Blog.py /app/

# Run the Python script when the container launches
CMD ["python", "Qilin_Blog.py"]