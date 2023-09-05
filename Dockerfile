# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install Firefox and other required dependencies
RUN apt-get update && apt-get install -y firefox-esr

# Install X11 utilities (for Xvfb)
RUN apt-get install -y xvfb

# Copy the script and requirements file into the container
COPY Groups/Qilin_Blog.py /app/Qilin_Blog.py
COPY Groups/sample2.py /app/sample2.py
COPY requirements.txt /app/requirements.txt

# Install required Python dependencies
RUN pip install -r requirements.txt

# Set up the display for Firefox using Xvfb
ENV DISPLAY=:99

# Start Xvfb and Firefox using a shell script
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh
CMD ["/app/start.sh"]
