import socket

print("🔍 Simple Network Scanner")

target = input("Enter target IP (e.g., 127.0.0.1): ")
ports = [21, 22, 80, 443]

print(f"\nScanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN]   Port {port}")
    else:
        print(f"[CLOSED] Port {port}")

    sock.close()

print("\n✅ Scan Completed")
