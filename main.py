from art import *
from pick import pick
import time
from simple_term_menu import TerminalMenu
from ping3 import ping

def createServer():
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
    print("IP: " + HOST)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    
                    conn.sendall(data)

def spam():
    ip = input('IP to spam: ')
    while True:
        ping(ip)

tprint("[_-Ghost V1-_]")
print("The creator of this program is not responsible for what you do!\n")

options = input("[1] Spam Ping [2] Create test server ")
if options == 1:
     spam
if options == 2:
    createServer
spam()