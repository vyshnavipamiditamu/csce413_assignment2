#!/usr/bin/env python3
"""
Port Scanner - Starter Template for Students
Assignment 2: Network Security

This is a STARTER TEMPLATE to help you get started.
You should expand and improve upon this basic implementation.

TODO for students:
1. Implement multi-threading for faster scans
2. Add banner grabbing to detect services
3. Add support for CIDR notation (e.g., 192.168.1.0/24)
4. Add different scan types (SYN scan, UDP scan, etc.)
5. Add output formatting (JSON, CSV, etc.)
6. Implement timeout and error handling
7. Add progress indicators
8. Add service fingerprinting
"""

import socket
import sys


def scan_port(target, port):
    """Scan a single port using the timeout clue."""
    try:
        # Create the socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Apply Clue: Set timeout to 1 second (per the tips)
        sock.settimeout(1.0)
        
        # Try to connect
        result = sock.connect_ex((target, port))
        
        # Close immediately
        sock.close()
        
        # Return True if the port is open (result 0)
        return result == 0
    except:
        return False


def scan_range(target, start_port, end_port):
    open_ports = []

    print(f"[*] Scanning {target} from port {start_port} to {end_port}")

    return open_ports


def main():
    """Main function to handle command-line arguments"""
    
    # Check if at least the target IP is provided
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <target_ip> [start_port] [end_port]")
        print("Example: python3 main.py 172.20.0.10 1 10000")
        sys.exit(1)

    # 1. Get the target IP
    target = sys.argv[1]

    # 2. Get the start port (default to 1 if not provided)
    if len(sys.argv) > 2:
        start_port = int(sys.argv[2])
    else:
        start_port = 1

    # 3. Get the end port (default to 1024 if not provided)
    if len(sys.argv) > 3:
        end_port = int(sys.argv[3])
    else:
        end_port = 1024

    print(f"[*] Starting port scan on {target} from port {start_port} to {end_port}")

    # Call the scanning function with the correct range
    open_ports = scan_range(target, start_port, end_port)

    # Display results
    print(f"\n[+] Scan complete!")
    print(f"[+] Found {len(open_ports)} open ports:")
    for port in open_ports:
        print(f"    Port {port}: open")


if __name__ == "__main__":
    main()
