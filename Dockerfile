# File name: Dockerfile
FROM rayproject/ray:2.5.0

# Set working directory
WORKDIR /serve_app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app.py
COPY app.py /serve_app/app.py

# Run ray serve
RUN serve run -p 1456 app:generator_app