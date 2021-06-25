import socket
from thread import Mythread
import json
import os


address = "127.0.0.1"
port = 5052

s = socket.socket()
s.bind((address,port))
s.listen(5)


    



while(True):
    print("Main server is Active")
    arr = os.listdir('Server_Files')
    c_s, addr = s.accept()
    client_thread = Mythread(c_s,arr)
    client_thread.start()







