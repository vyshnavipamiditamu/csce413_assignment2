## MITM

## Overview
This directory contains the implementation and findings for the Man-in-the-Middle (MITM) portion of the assignment. The objective was to intercept and analyze communication between the Web Application and the MySQL Database containers to identify security vulnerabilities.

## Implementation Details
- **Target Interface**: Docker bridge network interface.
- **Capture Tool**: `tcpdump` was utilized to monitor traffic on Port 3306 (MySQL).
- **Methodology**: By sniffing the internal bridge network, I captured raw TCP packets exchanged between the application and the database to observe data in transit.

## Findings & Vulnerability Analysis
- **Vulnerability**: The database communication is entirely unencrypted, transmitting data in Plaintext SQL.
- **Evidence**: The captured logs (stored in this directory) reveal cleartext SQL queries, including sensitive user information and authentication attempts.
- **Impact**: An attacker with network access can perform credential harvesting or data exfiltration by sniffing unencrypted traffic, potentially compromising the entire database.

## Deliverables
- **Captured Traffic**: The raw packet dump (`captured_traffic.txt`) showing the intercepted SQL queries.
- **Vulnerability Report**: This README serves as the explanation of the vulnerability and its impact as required.

## Remediation
To secure this communication, the connection should be encrypted using **TLS/SSL**, and the database should be restricted to a private internal network segment with strict access control lists (ACLs).
