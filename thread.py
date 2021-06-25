
from threading import Thread
import socket
import json
import textwrap
import os




class Mythread(Thread):
    def __init__(self,c_s,files):
        Thread.__init__(self)
        self.c_s = c_s
        self.FORMAT = "utf-8"
        self.files = files
        self.list = []

    def bytes(self,string,x):
        while(True):
            if(len(string)<x):
                string = "0"+string
            else:
                return string
    
    def send_files_list(self):
        list = json.dumps(self.files)
        self.c_s.send("0x0010".encode(self.FORMAT))
        string = self.bytes(str(len(self.files)),2)
        self.c_s.send(string.encode(self.FORMAT))
        self.c_s.send(list.encode(self.FORMAT))

    def Chunck_creater(self,data,x):
        while(True):
            self.list = textwrap.wrap(data, x)
            if(len(self.list[0])<97):
                break
            x=x-1




    def  send_specific_file_round2(self,counter):
        for items in range(counter):
            self.c_s.send("0x0012".encode(self.FORMAT))
            string = self.bytes(str(items),2)
            self.c_s.send(string.encode(self.FORMAT))
            self.c_s.send(self.list[items].encode(self.FORMAT))


        
        



    def send_specific_file_round1(self):
        file_name = self.c_s.recv(1024).decode(self.FORMAT)
        if file_name in self.files:
            file = open("Server_Files/"+file_name)
            data = file.read()
            data_bytes = len(data.encode("utf-8"))
            self.Chunck_creater(data,data_bytes)
            count = int((data_bytes/100)+1)
            self.c_s.send("0x0011".encode(self.FORMAT))
            self.c_s.send(file_name.encode(self.FORMAT))
            string = self.bytes(str(data_bytes),4)
            self.c_s.send(string.encode(self.FORMAT))
            self.send_specific_file_round2(count)


    def run(self):
        packet_offset = self.c_s.recv(1024).decode(self.FORMAT)
        if(packet_offset == "0X0000"):
            self.send_files_list()
        if(packet_offset == "0x0001"):
            self.send_specific_file_round1()
        
        


    
            
  
