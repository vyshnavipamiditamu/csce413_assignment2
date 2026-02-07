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


def scan_port(target, port, timeout=1.0):
    """
    Scan a single port on the target host

    Args:
        target (str): IP address or hostname to scan
        port (int): Port number to scan
        timeout (float): Connection timeout in seconds

    Returns:
        bool: True if port is open, False otherwise
    """
    try:
        # TODO: Create a socket
        # TODO: Set timeout
        # TODO: Try to connect to target:port
        # TODO: Close the socket
        # TODO: Return True if connection successful

        pass  # Remove this and implement

    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def scan_range(target, start_port, end_port):
    open_ports = []

    # Print the correct ports being scanned
    print(f"[*] Scanning {target} from port {start_port} to {end_port}")
    
    # Use the range provided by the user
    for port in range(start_port, end_port + 1):
        # We will implement the actual 'scan_port' logic in the next step
        if scan_port(target, port):
            open_ports.append(port)
            print(f"    [+] Port {port} is open")

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
