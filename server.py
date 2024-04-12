# Server Side Code
import socket
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('0.0.0.0', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
# Wait for a connection
print('Waiting for a Connection')
connection, client_address = sock.accept()
try:
  print('Connection from', client_address)
  # Receive the data in small chunks and retransmit it
  while true:
    data = connection.recv(16)
    print('Received "%s"' % data)
    if data:
      print('Sending Data back to the Client')
      connection.sendall(data)
    else:
      print('No Data from', client_address)
# 24/7
except:
  time.sleep(1)
  print('Running 24/7')
