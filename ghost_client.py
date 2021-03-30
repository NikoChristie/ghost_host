from os import F_TEST, terminal_size
import socket
from typing import get_type_hints
import pyautogui

HOST = '10.0.0.150' # The server's hostname or IP address
PORT = 65432        # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST, PORT))
    while True:
        s.sendall(b' ')
        data = s.recv(1024)
        
        data = data.decode('ascii')

        if len(data) == 1:
            print(f'{data} : {hex(ord(data))}')

        pyautogui.press(data)