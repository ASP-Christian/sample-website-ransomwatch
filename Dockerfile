# Use a base image with Tor, Firefox, and geckodriver installed
FROM debian:bullseye-slim

# Install Python and other dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip tor firefox-esr && \
    apt-get clean

# Install dependencies
RUN apt-get update && \
    apt-get install -y tor firefox-esr && \
    apt-get clean

# Download and install geckodriver
RUN apt-get install -y wget && \
    GECKODRIVER_VERSION=$(wget -qO- https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep '"tag_name":' | sed -E 's/.*"v(.*)".*/\1/') && \
    wget https://github.com/mozilla/geckodriver/releases/download/v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz -O /tmp/geckodriver.tar.gz && \
    tar -C /opt -xzf /tmp/geckodriver.tar.gz && \
    rm /tmp/geckodriver.tar.gz && \
    ln -s /opt/geckodriver /usr/local/bin/geckodriver

# Set environment variables for Tor and geckodriver
ENV TOR_SKIP_LAUNCH=1
ENV PATH="/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/bin"

# Copy your script and any other files into the container
COPY Groups/Qilin_Blog.py /app/Qilin_Blog.py

# Set the working directory
WORKDIR /app

# Start your script when the container starts
CMD ["python", "Qilin_Blog.py"]
