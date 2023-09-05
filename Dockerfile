# Use an official Selenium with Python runtime
FROM selenium/standalone-python:3.8

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the Python script into the container
COPY Groups/Qilin_Blog.py /app/Qilin_Blog.py

# Run the Python script when the container launches
CMD ["python", "Qilin_Blog.py"]
