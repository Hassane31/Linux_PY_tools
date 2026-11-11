import socket
from IPy import IP

def checkIp(ip) :
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipadress,port):
  try:
       sock = socket.socket()
       sock.settimeout(0.5)
       sock.connect((ipadress, port))
       print('[+] Port ' + str(port) + ' is open :')
  except:
       print('[+] Port '+ str(port) +' not available :')


ipadress = input('[+] Enter target to scan : ')
ip_converted = checkIp(ipadress)


for port in range(75,85):
    scan_port(ip_converted,port)