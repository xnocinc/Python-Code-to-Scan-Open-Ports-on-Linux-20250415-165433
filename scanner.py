import socket
import sys

host = sys.argv[1]
ports = list(map(int, sys.argv[2].split('-')))
for port in range(ports[0], ports[1]+1):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    if not s.connect_ex((host,port)):
        print(f"Port {port} is open")
    s.close()