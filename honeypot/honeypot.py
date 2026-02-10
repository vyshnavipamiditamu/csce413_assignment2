import socket
from logger import log_attempt

def start_trap():
    # Requirement: Simulate a real service (SSH Banner)
    BANNER = b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5\r\n"
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 22))
    server.listen(5)
    
    print("[+] SSH Honeypot is active on port 22...")

    while True:
        client, addr = server.accept()
        ip, port = addr
        client.send(BANNER) # Be convincing
        
        try:
            # Capture the raw SSH connection data
            data = client.recv(1024).decode('utf-8', errors='ignore')
            log_attempt(ip, port, "admin", data.strip())
            client.send(b"Access denied\n")
        finally:
            client.close()

if __name__ == "__main__":
    start_trap()
