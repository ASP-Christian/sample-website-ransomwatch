FROM python:3.8

# Install Tor and other dependencies
RUN apt-get update && apt-get install -y tor

# Copy your code and requirements into the container
COPY . /app
WORKDIR /app

# Install Python packages
RUN pip install -r requirements.txt

# Set the entry point command
CMD ["python", "Groups/Qilin_Blog.py"]
