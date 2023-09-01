# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the script and requirements file into the container
COPY Groups/Qilin_Blog.py /app/Qilin_Blog.py
COPY requirements.txt /app/requirements.txt

# Install required dependencies
RUN pip install -r requirements.txt

# Install TOR
RUN apt-get update && \
    apt-get install -y tor && \
    apt-get clean

# Expose the necessary port for TOR (if needed)
# EXPOSE 9050

# Run the script when the container starts
CMD ["python", "Qilin_Blog.py"]
