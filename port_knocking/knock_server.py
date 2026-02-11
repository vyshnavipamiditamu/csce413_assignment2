import socket

# Configuration matching your README and Client
KNOCK_SEQUENCE = [7000, 8000, 9000]
TARGET_PORT = 2222
current_step = 0

def monitor_knocks():
    global current_step
    print(f"Monitoring for knock sequence: {KNOCK_SEQUENCE}...")

    while True:
        # Listen for the next port in the sequence
        expected_port = KNOCK_SEQUENCE[current_step]
        
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('0.0.0.0', expected_port))
                s.listen(1)
                s.settimeout(10) # 10 second window per knock
                conn, addr = s.accept()
                print(f"Correct knock on port {expected_port} from {addr[0]}")
                current_step += 1
        except socket.timeout:
            print("Sequence timed out. Resetting.")
            current_step = 0
            continue
        except Exception as e:
            current_step = 0
            continue

        # If full sequence is hit
        if current_step == len(KNOCK_SEQUENCE):
            print(f"Sequence complete! Opening port {TARGET_PORT}...")
            # In a real scenario, this is where you'd trigger 'iptables'
            # For this lab, we log the success to prove implementation
            print(f"SUCCESS: Access granted to port {TARGET_PORT}")
            current_step = 0

if __name__ == "__main__":
    monitor_knocks()
