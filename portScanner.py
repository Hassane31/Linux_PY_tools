import socket
from IPy import IP



def get_banner(s):
    return s.recv(1024)


def checkIp(ip) :
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan(target):
    ip_converted = checkIp(target)
    print('\n[-_0 Scanning target '+ str(target)+' :')
    for port in range(1, 100):
        scan_port(ip_converted, port)

def scan_port(ipadress,port):
  try:
       sock = socket.socket()
       sock.settimeout(0.5)
       sock.connect((ipadress, port))
       try:
           banner = get_banner(sock)
           print('[+]Open port '+str(port)+ ' + '+str(banner.decode().strip('\n')))
       except :
           print('[+]Open port '+str(port))
  except:
      pass

targets = input('[+] Enter target/s to scan(multiple targests with ,) : ')
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip('  '))
else:
    scan(targets)

