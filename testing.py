def bytes_2(string):
    while(True):
        if(len(string)<2):
            string = "0"+string
        else:
            return string


a = "1"
print(len(a))
string = bytes_2(a)
print(len(string))