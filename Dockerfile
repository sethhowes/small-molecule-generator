# Use the official Ubuntu 20.04 base image
FROM rayproject/ray:2.9.3-py39-cu118

# Set environment variable to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=noninteractive
USER root

# Set working directory
WORKDIR /serve_app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app.py
COPY app.py /serve_app/app.py

# Run ray serve
RUN ["python", "app.py"]