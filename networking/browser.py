import socket

# Classical socket approach
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

print('\nsockets:')
while True:
  data = mysock.recv(512)
  if (len(data) < 1):
    break
  print(data.decode(), end='')

mysock.close()

print('\nurllib:')
# Urllib simplifies http calls
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
for line in fhand:
  print(line.decode().strip())
