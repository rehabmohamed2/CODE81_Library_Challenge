import socket
import sys

def test_port_connection(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        print(f"Error testing connection: {e}")
        return False

print("Testing basic connection to localhost:9007...")
if test_port_connection("localhost", 9007):
    print("SUCCESS: Port 9007 is accepting connections")
else:
    print("FAILED: Cannot connect to port 9007")

print("Testing connection to 127.0.0.1:9007...")
if test_port_connection("127.0.0.1", 9007):
    print("SUCCESS: Port 9007 is accepting connections on 127.0.0.1")
else:
    print("FAILED: Cannot connect to port 9007 on 127.0.0.1")