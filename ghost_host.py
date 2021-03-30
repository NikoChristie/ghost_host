import socket
from getkey import getkey

special_chars = {
    0x7f : 'backspace'
}

HOST = '10.0.0.150' # '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:

            key = getkey()

            data = conn.recv(1024) # useless

            # print(f'{list(special_chars.keys())} -> {ord(key)}')

            if ord(key) in list(special_chars.keys()):
                key = special_chars[ord(key)]
            
            if len(data) == 0:
                print(f'{key} : {ord(key)}')

            if not data:
                break
            conn.sendall(key.encode('ascii'))