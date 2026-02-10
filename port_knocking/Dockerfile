FROM ubuntu:22.04

# Install iptables and SSH
RUN apt-get update && apt-get install -y iptables openssh-server iproute2 && rm -rf /var/lib/apt/lists/*

# Setup SSH on Port 2222
RUN mkdir -p /var/run/sshd && echo 'root:password123' | chpasswd && \
    sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Stateless iptables logic:
# - Port 1234 sets 'STAGE1'
# - Port 5678 checks 'STAGE1', sets 'STAGE2'
# - Port 9012 checks 'STAGE2', sets 'PASSED'
# - Port 2222 is ONLY open if IP is in 'PASSED'
CMD service ssh start && \
    iptables -N KNOCKING && \
    iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT && \
    iptables -A INPUT -p tcp --dport 2222 -m recent --rcheck --name PASSED --seconds 60 -j ACCEPT && \
    iptables -A INPUT -p tcp --dport 2222 -j REJECT && \
    iptables -A INPUT -p tcp --dport 9012 -m recent --rcheck --name STAGE2 -m recent --set --name PASSED -j ACCEPT && \
    iptables -A INPUT -p tcp --dport 5678 -m recent --rcheck --name STAGE1 -m recent --set --name STAGE2 -j ACCEPT && \
    iptables -A INPUT -p tcp --dport 1234 -m recent --set --name STAGE1 -j ACCEPT && \
    sleep infinity
