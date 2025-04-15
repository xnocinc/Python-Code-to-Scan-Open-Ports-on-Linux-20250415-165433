**Reasoning Extracted**

```
Okay, the user wants a Python script to scan open ports on a Linux machine. Let me think about how to approach this. I remember that port scanning typically involves trying to connect to each port on a target host and seeing if the connection is accepted. 

First, I'll need to use the socket module in Python. The basic idea is to create a socket, attempt to connect to a specific port, and check if the connection is successful. If there's no error, the port is open.

Wait, but how do I handle multiple ports efficiently? Maybe loop through a range of ports. The user didn't specify a range, so perhaps scan from 1 to 1024, which covers common ports. Alternatively, maybe let the user input the target IP and port range. But the task says to return the code, so maybe the code should take command-line arguments?

Looking at the output example, the user wants the code only, without explanations. So I should structure the code to take arguments. Let me see: maybe using sys.argv to get the target IP and port range. Like, the user runs the script with something like python portscanner.py 192.168.1.1 1-1024.

So, the code should parse the port range. Split the second argument on '-', then loop from start to end port.

Wait, but error handling is important here. What if the user inputs invalid ports or the IP is unreachable? Maybe it's okay to keep it simple without too much error handling since the task says to write clean and complete code, but not necessarily with extensive error checking. 

The main steps would be:

1. Import socket and sys.
2. Check if the correct number of arguments are provided.
3. Parse the target IP and port range.
4. For each port in the range, try to connect.
5. If connection is successful, print that the port is open.

So the code structure would be something like:

import socket
import sys

if len(sys.argv) != 3:
    print("Usage: python portscanner.py <host> <start_port-end_port>")
    sys.exit()

host = sys.argv[1]
port_str = sys.argv[2].split('-')
start = int(port_str[0])
end = int(port_str[1])

for port in range(start, end+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # To avoid hanging indefinitely
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()

Wait, using connect_ex instead of connect because it returns an error code, which is better for checking. Also, set a timeout so that it doesn't take too long for closed ports.

Hmm, that should work. Let me check if I missed anything. The user is on Linux, so maybe socket operations are okay. The code should be straightforward. Also, the output is only the code, so no extra comments or explanations. 

I think that's it. Let me write the code accordingly.
```