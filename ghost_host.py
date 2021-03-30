import socket
from getkey import getkey, keys

HOST = '' # Host IP
PORT = 65432 # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:

            data = conn.recv(1024) # useless

            if not data:
                break

            key = keys.name(getkey())
            print(key)

            if key is not None:

                key = key.lower()

                if 'shift_' in key:
                    key = key.split('shift_')[1].upper()

                print(f'{key}', end='')
                
                conn.sendall(key.encode('ascii'))
            else:
                print('key is None')
                conn.sendall(''.encode('ascii'))
