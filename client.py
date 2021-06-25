import socket
import json

address = "127.0.0.1"
port = 5052
FORMAT = "utf-8"
list = []

def get_list(s):
    s.send("0X0000".encode(FORMAT))
    packet_offset = s.recv(1024).decode(FORMAT)
    No_of_items = s.recv(1024).decode(FORMAT)
    J_list = s.recv(1024).decode(FORMAT)
    list = json.loads(J_list)
    for items in list:
        print(items)

def download_file(s):
    String = input("Enter  file name: ")
    s.send("0x0001".encode(FORMAT))
    s.send(String.encode(FORMAT))
    packet_offset = s.recv(1024).decode(FORMAT)
    File_name = s.recv(1024).decode(FORMAT)
    File_bytes = s.recv(1024).decode(FORMAT)
    count = int((int(File_bytes)/100)+1)
    list = download_file2(s,count)
    file = open("Client_download/"+File_name,"w")
    for element in list: 
        data = file.write(element+"\n")

def download_file2(s,count):
    for items in range(count):
        packet_offset = s.recv(1024).decode(FORMAT)
        SYN = s.recv(1024).decode(FORMAT)
        data = s.recv(1024).decode(FORMAT)
        list.append(data)
    return list


    
s = socket.socket()
s.connect((address,port))

value = int(input("Enter 1 to request list_of_files OR 2 to mention name of specific file: "))
if(value == 1):
    get_list(s)
if(value == 2):
    download_file(s)