FROM ubuntu:latest

# Install Tor and other dependencies
RUN apt-get update && apt-get install -y tor firefox

# Copy your script to the container
COPY Groups/Qilin_Blog.py /app/Qilin_Blog.py

CMD ["bash"]
