#!/usr/bin/env python3

import socket
import sys

socket_path = sys.argv[1]
msg = sys.stdin.buffer.read()

SIZE=1024

client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client.connect(socket_path)
client.send(msg)
response, address = client.recvfrom(SIZE)
sys.stdout.buffer.write(response)
