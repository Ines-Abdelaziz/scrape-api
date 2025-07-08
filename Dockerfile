# Use browserless Chrome with matched Chrome + Chromedriver
FROM browserless/chrome:1.57-chrome-stable

# Use root for installation
USER root

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir flask selenium

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Expose Flask port
EXPOSE 5000

# Run your app
CMD ["python3", "api.py"]
