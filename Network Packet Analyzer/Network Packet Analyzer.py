from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        protocol = ip_layer.proto
        
        print(f"\n[+] New Packet:")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        
        if protocol == 6:  # TCP protocol number
            print("Protocol: TCP")
        elif protocol == 17:  # UDP protocol number
            print("Protocol: UDP")
        elif protocol == 1:  # ICMP protocol number
            print("Protocol: ICMP")
        else:
            print(f"Protocol: {protocol}")

        # Check if the packet has a TCP or UDP layer and print payload data
        if TCP in packet or UDP in packet:
            print(f"Payload:\n{bytes(packet[TCP].payload)}")

# Start sniffing packets
print("Starting packet sniffing... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0)
