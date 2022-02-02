import requests
import socket
from datetime import datetime
import webbrowser

#port = ":3000"
port = ":80"
api = "/find"

host_name = socket.gethostname()
net = socket.gethostbyname(host_name)
print("my ip is: " + net)

net1 = net.split('.')
print(net1)
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a

st1 = 2
en1 = 100
en1 = en1 + 1
#t1 = datetime.now()

def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   print(addr)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,80))
   if result == 0:
      return 1
   else :
      return 0

def run1():
   for ip in range(st1,en1):
      addr = net2 + str(ip)
      if (scan(addr)):
         print (addr , "is live")
         response = requests.get("http://" +addr +port +api)
         value = print(response.text)
         value = response.text
         print(value)
         #test
         if value == "switch":
             print("success")
             print("http://" +addr +port)
             webbrowser.open("http://" +addr +port)
         else:
             print("someother ip")
             
         
         
         
run1()
#

#response = requests.get("http://" +ip +port +api)
#response = requests.get("http://192.168.1.3:3000/test")
#print(response.status_code0)
#print(response)
#print(response.text)