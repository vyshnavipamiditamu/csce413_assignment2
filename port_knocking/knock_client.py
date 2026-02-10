import socket, sys, time

def knock(target):
    # Requirement: Knock sequence 1234, 5678, 9012
    for port in [1234, 5678, 9012]:
        try:
            # Touch the port to trigger the 'recent' module
            with socket.create_connection((target, port), timeout=0.2): pass
        except: pass
        print(f"Knocked on {port}")
        time.sleep(0.5)

if __name__ == "__main__":
    if len(sys.argv) > 1: knock(sys.argv[1])
