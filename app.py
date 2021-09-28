from threading import Thread
import time, json
from socket import socket, AF_INET, SOCK_STREAM
from http import client
from urllib.parse import urlencode
from urllib.request import Request, urlopen

a_socket = socket(AF_INET, SOCK_STREAM)
url = 'http://127.0.0.1:5000'


f = open('resources.txt')
resources = []
for i in f:
    ip, port = i.strip().split(':')
    resources.append((ip,int(port)))

print(resources)

def check(ip, port):
    if a_socket.connect_ex((ip, port)):
        request = Request(url, data=json.dumps({'failed': f'{ip}:{port}'}).encode('utf-8'))
        request.add_header('Content-Type', 'application/json')
        resp = urlopen(request)

while True:
    for ip,port in resources:
        t = Thread(target=check, args=(ip,port))
        t.start()
    time.sleep(2)