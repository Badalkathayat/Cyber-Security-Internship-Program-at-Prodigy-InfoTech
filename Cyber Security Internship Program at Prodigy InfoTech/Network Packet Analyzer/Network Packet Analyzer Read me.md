Network Packet Analyzer

This is a simple yet powerful packet sniffer tool developed in Python. The tool captures and analyzes network packets, displaying relevant information such as source and destination IP addresses, protocols, and payload data. This tool is intended for educational purposes only.

Features

- Captures live network packets.
- Displays source and destination IP addresses.
- Identifies and shows the protocol used (TCP, UDP, ICMP).
- Displays payload data for TCP and UDP packets.

Prerequisites

- Python 3.x
- `scapy` library

Installation

1. Clone the repository:

   bash
   git clone https://github.com/Badalkathayat/Network-Packet-Analyzer.git
   cd Network-Packet-Analyzer
   

2. Install the required library:

   bash
   pip install scapy
   

## Usage

1. Run the packet sniffer tool:

   bash
   sudo python packet_sniffer.py
   

   > **Note:** You might need to run the script with administrative privileges (e.g., using `sudo` on Linux) to capture packets.

2. The tool will start capturing packets and display information such as source and destination IP addresses, protocols, and payload data.

3. To stop the tool, press `Ctrl+C`.

## Example Output

plaintext
Starting packet sniffing... Press Ctrl+C to stop.

[+] New Packet:
Source IP: 192.168.1.2
Destination IP: 192.168.1.1
Protocol: TCP
Payload:
b'\x16\x03\x01\x02\x00\x01\x00\x01\xfc\x03\x03\x99\xd3\xc1\x11...'

[+] New Packet:
Source IP: 8.8.8.8
Destination IP: 192.168.1.2
Protocol: ICMP

Ethical Considerations

This tool is designed for educational purposes. Unauthorized use of packet sniffing tools on networks where you do not have permission is illegal and unethical. Please ensure you have proper authorization before using this tool on any network.

Contribution

Feel free to fork this repository, submit issues, or send pull requests. Contributions are welcome!

License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


You can copy this into a `README.md` file and include it in your GitHub repository. This will give users a clear understanding of the project, how to set it up, and the ethical considerations involved.
