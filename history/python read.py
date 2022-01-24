'''
Created on 2021年11月12日

@author: user
'''

import os
import time

if __name__ == '__main__':
    my_bytes = None
    my_bytes_array = []
    file_r_path = input("open file name:")
    if file_r_path != "":
        file_size = os.path.getsize(file_r_path) 
        print('File Size:', file_size, 'bytes')
        
        time.sleep(5)
        
        """
        filesize = 0
        with open(file_r_path, "rb")as f:
            my_bytes = f.read()
        my_bytes_array.append(my_bytes)
        filesize = 1
        print(my_bytes[0:file_size])
        print(filesize)
        """
        file_start_size = (file_size//100)*100
        file_end_size = file_size-file_start_size
        with open(""+file_r_path, "rb") as f:
            my_bytes = f.read()
        #試試看:跟剛才的版本,看到的my_bytes前一百項,有什麼不同?
        for i in range(0,file_start_size,100):
            print(my_bytes[i+0:i+100])
            print("\n")
            time.sleep(0.03)
        ii = i
        time.sleep(2)
        for i in range(ii,file_end_size):
            print(my_bytes[i+0:i+100])
            print("\n")
            time.sleep(0.03)
        print("-==-"*30)
        print("file_size",file_size,"\n")

        data = my_bytes
        with open("bin.py", "wb") as f:
            f.write(data)
    
'''
Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
with open("bin.py", "r") as f:
    data = f.read()
print(data)
exec(open("bin.py").read())
