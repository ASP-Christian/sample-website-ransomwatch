FROM python:3.8

# Install Tor and other dependencies
RUN apt-get update && apt-get install -y tor
RUN pip install -r requirements.txt

# Copy your code into the container
COPY . /app
WORKDIR /app

# Define the entry point command
CMD ["python", "Groups/Qilin_Blog.py"]
