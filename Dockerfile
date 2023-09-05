# Use an official Selenium base image with Firefox and geckodriver
FROM selenium/standalone-firefox:latest

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY Groups/Qilin_Blog.py /app/Qilin_Blog.py

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run the Python script when the container launches
CMD ["python", "Qilin_Blog.py"]
