import logging
import os

# Wire logging to the required logs directory
LOG_FILE = "/app/logs/honeypot.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def log_attempt(ip, port, user, password):
    # Requirement: Log IP, Port, and Authentication attempts
    entry = f"INTRUSION DETECTED | Source: {ip}:{port} | User: {user} | Pass: {password}"
    logging.info(entry)
    print(f"[*] {entry}")
