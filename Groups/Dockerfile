# Use a base image that includes TOR and Python
FROM some-tor-python-image

# Copy your script to the container
COPY Groups/Qilin_Blog.py /app/Qilin_Blog.py

# Set the working directory
WORKDIR /app

# Set up any additional dependencies
RUN pip install pandas selenium

# Define the command to run your script
CMD ["python", "Qilin_Blog.py"]
