import socket
from datetime import datetime

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout per port
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0  # True if port is open
    except socket.error:
        return False


def scan_range(target, start_port, end_port):
    print(f"\nScanning {target} from port {start_port} to {end_port}")
    print(f"Started at: {datetime.now()}\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            open_ports.append(port)
            print(f"Port {port}: OPEN")

    print(f"\nScan completed at: {datetime.now()}")
    print(f"Open ports found: {open_ports if open_ports else 'None'}")
    return open_ports


if __name__ == "__main__":
    target = input("Enter target IP or hostname (e.g., 127.0.0.1): ")
    start_port = int(input("Enter start port (e.g., 1): "))
    end_port = int(input("Enter end port (e.g., 100): "))

    scan_range(target, start_port, end_port)