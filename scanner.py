import socket

Common_ports = [
    21, #FFTP
    22, #SSH
    23, #tELNET
    80, #HTTP
    443, #HTTPS
    110, #POP3
    143, #IMAP  
    53, 
    445,
    3306, #mySQL 
    3389,
    5432, #PostgreSQL
    6379, #Redis
]

# Function to load targets from a text file
def load_targets(ip_list_txt):
    targets = []
    with open(ip_list_txt, "r") as file:
        for line in file:
            ip_address = line.strip()
            if ip_address:
                targets.append(ip_address)
    return targets

# Function to scan ports for a given IP address
def scan_ports(ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)  # Set a timeout for the connection attempt

    results = sock.connect_ex((ip_address, port))  # Attempt to connect to the specified port
    sock.close()

    if results == 0:
        return True  # Port is open
    else:
        return False  # Port is closed

def scan_host(ip_address, ports):
    results = []
    for port in ports:
        is_open = scan_ports(ip_address, port)
        results.append({
            "ip_address": ip_address,
            "port": port,
            "status": "open" if is_open else "closed"
        })
    return results

def main():
    targets = load_targets("ip_list.txt")
    ports_to_scan = Common_ports  # Example ports to scan

    with open("Scan_results.txt", "w") as file:
        for target in targets:
            scan_results = scan_host(target, ports_to_scan)
            for result in scan_results:
                print(f"IP: {result['ip_address']}, Port: {result['port']}, Status: {result['status']}")
                file.write(f"IP: {result['ip_address']}, Port: {result['port']}, Status: {result['status']}\n")


# targets = load_targets("ip_list.txt")
# print(targets)
if __name__ == "__main__":
    main()

