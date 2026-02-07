#!/usr/bin/env python3
import socket
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def get_banner(sock):
    """Attempt to read the service banner from an open port."""
    try:
        # Send a basic probe or just wait for a greeting
        sock.send(b'Hello\r\n')
        banner = sock.recv(1024).decode(errors='ignore').strip()
        return banner if banner else "No banner"
    except:
        return "Unknown Service"

def scan_port(target, port, timeout=1.0):
    """Performs a TCP connect scan on a single port."""
    try:
        # Create socket (AF_INET = IPv4, SOCK_STREAM = TCP)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            # connect_ex returns 0 for a successful connection
            result = s.connect_ex((target, port))
            
            if result == 0:
                banner = get_banner(s)
                return (port, True, banner)
    except:
        pass
    return (port, False, None)

def scan_range(target, start_port, end_port, threads=100):
    """Scans a range using a ThreadPoolExecutor for speed."""
    open_ports = []
    print(f"[*] Scanning {target} (Ports {start_port}-{end_port}) with {threads} threads...")
    start_time = datetime.now()

    with ThreadPoolExecutor(max_workers=threads) as executor:
        # Map the scan_port function across the port range
        futures = [executor.submit(scan_port, target, p) for p in range(start_port, end_port + 1)]
        
        for future in futures:
            port, is_open, banner = future.result()
            if is_open:
                print(f"    [+] Port {port:5}: OPEN | Service: {banner}")
                open_ports.append((port, banner))

    duration = datetime.now() - start_time
    print(f"[*] Scan duration: {duration}")
    return open_ports

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <target> [start_port] [end_port] [threads]")
        print("Example: python3 main.py 172.20.0.10 1 10000 200")
        sys.exit(1)

    target = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024
    threads = int(sys.argv[4]) if len(sys.argv) > 4 else 100

    print(f"\n{'-'*50}\nStarting scan on {target}\n{'-'*50}")
    open_ports = scan_range(target, start_port, end_port, threads)
    
    print(f"\n[+] Scan complete! Found {len(open_ports)} open ports.")

if __name__ == "__main__":
    main()
