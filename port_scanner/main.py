import socket
import sys
import time

def scan_port(target, port, timeout=1.0):
    """
    Requirement: Perform TCP connect scans and Service/banner detection.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((target, port))
            
            if result == 0:
                # Requirement: Service/banner detection
                # Attempt to receive the first 1024 bytes of data from the port
                try:
                    # Some services require a small nudge to send a banner
                    s.send(b"Hello\r\n") 
                    banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                except:
                    banner = "No banner received"
                return True, banner
    except Exception:
        pass
    return False, None

def scan_range(target, start_port, end_port):
    open_ports = []
    print(f"[*] Scanning {target} from port {start_port} to {end_port}")
    
    for port in range(start_port, end_port + 1):
        is_open, banner = scan_port(target, port)
        if is_open:
            # Requirement: Display port number, state, and service
            print(f"    [+] Port {port:5}: OPEN | Service: {banner}")
            open_ports.append((port, banner))
    return open_ports

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <target_ip> [start_port] [end_port]")
        sys.exit(1)

    target = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    # Requirement: Display results with timing
    start_time = time.time()
    print(f"[*] Starting port scan on {target} at {time.strftime('%H:%M:%S')}")

    open_ports = scan_range(target, start_port, end_port)

    end_time = time.time()
    duration = end_time - start_time

    print(f"\n[+] Scan complete!")
    print(f"[+] Found {len(open_ports)} open ports.")
    print(f"[+] Total scan duration: {duration:.2f} seconds")

if __name__ == "__main__":
    main()
