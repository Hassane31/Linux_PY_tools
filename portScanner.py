import socket
from IPy import IP

port = 80

def scan_port(ipadress,port):
  try:
       sock = socket.socket()
       sock.connect((ipadress, port))
       print('[+] Port ' + str(port) + ' is open :')
  except:
       print('[+] Port '+ str(port) +'not available :')


ipadress = input('[+] Enter target to scan : ')


for port in range(1,10):
    scan_port(ipadress,port)