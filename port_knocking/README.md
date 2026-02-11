# Fix 1: Port Knocking Implementation

## Design Decisions
- **Protected Service**: SSH (Port 2222).
- **Knock Sequence**: A sequence of three ports (e.g., 7000, 8000, 9000) must be hit in order to open the firewall.
- **Security Logic**: The system remains closed by default to prevent port scanning and unauthorized access.

## Implementation Details
- **Server**: `knock_server.py` monitors connection attempts and dynamically updates iptables rules upon receiving a valid sequence.
- **Client**: `knock_client.py` automates the sequence of connection attempts to the target host.

## Security Analysis
- **Strengths**: Significantly reduces the attack surface by making the SSH port "invisible" to standard scanners.
- **Limitations**: Vulnerable to replay attacks if an attacker is sniffing the network traffic.

## Testing
1. Run `python3 knock_client.py --target <IP> --sequence 7000,8000,9000`.
2. Connect via `ssh user@<IP> -p 2222`.
