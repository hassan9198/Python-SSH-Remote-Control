# Controlling A Device Over Internet
import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Input prompt so the user can enter the IP address/Hostname of the server or client
server_address = input("Please enter the IP address: ")
# Input prompt so the user can enter the port number of the server or client
server_port = int(input("Please enter the port number: "))
# Connect to server
print("Connecting...")
sock.connect((server_address, server_port))
# Status if the connection is successful
print("Connected")
# Controlling the server
while True:
  # Input prompt so the user can enter the command to be sent to the server
  command = input("Please enter any command: ")
  # Send the command to the server
  sock.sendall(command.encode())
  # Receive the response from the server
  response = sock.recv(1024)
  # Print the response from the server
  print(response.decode())
  # Input prompt so the user can enter the time to wait before sending the next command
  time.sleep(int(input("Please enter the time to wait: ")))
