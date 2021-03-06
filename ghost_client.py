import socket
from typing import Text
import pyautogui

HOST = '' # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST, PORT))
    while True:
        s.sendall(b' ')
        data = s.recv(1024)
        
        data = data.decode('ascii')

        if len(data) == 1:
            print(f'{data} : {hex(ord(data))}')
        else:
            print(f'{data}')
        pyautogui.press(data)
