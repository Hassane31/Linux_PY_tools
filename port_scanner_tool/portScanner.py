import socket
from base64 import decode
from string.templatelib import convert

from IPy import IP


class portScan():
    banners = []
    open_ports = []
    def __init__(self,target,port_number):
        self.target = target
        self.port_number = port_number



    def checkIp(self) :
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan(self):
        for port in range(1, 100):
            self.scan_port(port)

    def scan_port(self,port):
      try:
           ip_converted = self.checkIp()
           sock = socket.socket()
           sock.settimeout(0.5)
           sock.connect((ip_converted, port))
           self.open_ports.append(port)
           try:
               banner = sock.recv(1024).decode().strip('\n').strip('\r')
               self.banners.append(banner)
           except :
               self.banners.append('  ')
               sock.close()
      except:
          pass

   # if __name__ == '__main__':
   #  targets = input('[+] Enter target/s to scan(multiple targests with ,) : ')
   #   if ',' in targets:
   #       for ip_add in targets.split(','):
   #           scan(ip_add.strip('  '))
   #   else:
   #      scan(targets)

