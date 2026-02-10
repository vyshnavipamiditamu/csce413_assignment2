#!/bin/bash
# demo.sh updated to use official SSH commands
TARGET_IP=$1

echo "[1/3] Testing SSH BEFORE knocking (Should fail)..."
ssh -o ConnectTimeout=3 root@$TARGET_IP -p 2222

echo "[2/3] Performing knock sequence..."
python3 knock_client.py $TARGET_IP

echo "[3/3] Testing SSH AFTER knocking (Should prompt for password)..."
echo "Note: Use password 'password123' if prompted."
ssh -o ConnectTimeout=5 root@$TARGET_IP -p 2222
