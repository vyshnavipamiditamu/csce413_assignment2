Readme file:
# Part 3: Port Knocking Implementation (Option C)

## Overview
This implementation uses a stateless, kernel-level port knocking mechanism via the Linux `iptables` **recent** module. 

## Implementation Details
- **Protected Service**: OpenSSH server running on port 2222.
- **Knock Sequence**: TCP attempts to ports 1234 -> 5678 -> 9012.
- **Mechanism**: 
  - The firewall starts by rejecting all traffic to port 2222.
  - As a client hits each port in the sequence, the `recent` module tracks the source IP and promotes it through several stages (STAGE1, STAGE2).
  - Upon completing the final knock, the IP is added to a `PASSED` list.
  - The firewall allows port 2222 access ONLY to IPs in the `PASSED` list for a 60-second window.

## Files
- `Dockerfile`: Configures the Ubuntu environment and the complex iptables logic.
- `knock_client.py`: A Python script that performs the TCP connections to the sequence ports.
- `demo.sh`: A shell script that demonstrates the "Before", "Knock", and "After" states.

## Testing
Run the following command within the directory:
```bash
./demo.sh <container_ip>

