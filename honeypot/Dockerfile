FROM python:3.11-slim

WORKDIR /app

# Copy ALL files from the current host directory to the container /app directory
COPY . .

# Create logs directory inside the container
RUN mkdir -p /app/logs

EXPOSE 22

# Run Python in unbuffered mode (-u) to see logs immediately
CMD ["python", "-u", "honeypot.py"]
