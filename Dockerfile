# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -U selenium pytz

# Install Firefox browser and the geckodriver
RUN apt-get update && apt-get install -y firefox-esr && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove && \
    wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz && \
    tar -xvzf geckodriver-v0.30.0-linux64.tar.gz && \
    chmod +x geckodriver && \
    mv geckodriver /usr/local/bin/ && \
    rm geckodriver-v0.30.0-linux64.tar.gz

# Install and configure TOR
RUN apt-get update && apt-get install -y tor
RUN echo "SOCKSPort 0.0.0.0:9150" >> /etc/tor/torrc

# Run the TOR service
CMD tor & sleep 5 && python your_script.py
