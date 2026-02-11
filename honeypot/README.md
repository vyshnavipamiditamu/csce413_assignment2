# Fix 2: SSH Honeypot Implementation

## Overview
This implementation features a custom-built SSH honeypot designed to detect and log unauthorized access attempts. It acts as a decoy service to monitor attacker behavior and gather threat intelligence.

## Design Decisions
- **Port**: The honeypot listens on port 2222, masquerading as a standard SSH service.
- **Logging Mechanism**: Every connection attempt, including the source IP, timestamp, and provided credentials, is captured and logged to `analysis.md`.
- **Response Strategy**: The honeypot is programmed to reject all authentication attempts after logging them, ensuring the attacker never gains actual shell access to the host.

## Files
- `honeypot.py`: The Python script using `socket` and `paramiko` to emulate the SSH handshake.
- `analysis.md`: A live forensic log where captured intrusion data is stored for review.
- `Dockerfile`: Containerizes the honeypot for easy deployment and isolation.

## Captured Attack Analysis
As documented in `analysis.md`, the honeypot successfully captured an intrusion attempt:
- **Timestamp**: 2026-02-10 05:30:31
- **Source IP**: 172.17.0.1
- **Observed Behavior**: Brute-force attempt using the username 'admin'.
