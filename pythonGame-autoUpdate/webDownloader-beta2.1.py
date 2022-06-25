import os
import time
import wget,sys
import urllib #urllib2.urlopen 

import requests

import threading

from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox

from cheakfile import cheakFile

root = Tk()
root.title("cheakUpdate")
bytes = 0                           # 設定初值
maxbytes = 10000                    # 假設下載檔案大小 
count = 0

fn = None
data = """
https://github.com/sam-teng/update-data/archive/refs/heads/main.zip
"""
""",
https://github.com/sam-teng/update-data/blob/main/pythonGame-autoUpdate/game_socket-client_2P-GUIv2.py,
https://github.com/sam-teng/update-data/blob/main/pythonGame-autoUpdate/game_socket-server_2P-GUIv2.py,
https://github.com/sam-teng/update-data/blob/main/pythonGame-autoUpdate/view.py

"""

def _exec():
    with open("updatefile.py","rb") as fr:
        fr = fr.read()
        print(fr)
        exec(fr)

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)#mode="indeterminate"
pb.pack(padx=10,pady=10)
pb["value"] = 0                     # Prograssbar初始值

def load():                         # 啟動Prograssbar
    pb["value"] = 0                 # Prograssbar初始值
    pb["maximum"] = maxbytes        # Prograddbar最大值
    
    loading()

def loading():                      # 模擬下載資料
    global bytes
    bytes += 200//len(data.split(","))   # 模擬每次下在500bytes
    pb["value"] = bytes             # 設定指針
    if bytes < maxbytes:
        pb.after(50,loading)        # 經過0.05秒繼續執行loading
    else:
        global count
        pram = """
        game_socket-client_2P-GUIv2.py,
        game_socket-server_2P-GUIv2.py,
        view.py

        """
        file_source = "temp/update-data-main/pythonGame-autoUpdate/"
        file_destination = "./"
        i = 1
        for arg in pram.split(","):
            if not cheakFile(arg,file_source+arg):
                if i == len(pram.split(",")):
                    tkinter.messagebox.showinfo("showinfo", "更新中請耐心等候")
                #更新目前檔案
                
                 
                get_files = os.listdir(file_source)
                 
                for g in get_files:
                    os.replace(file_source + g, file_destination + g)
            else:
                if i == len(pram.split(",")):
                    tkinter.messagebox.showinfo("showinfo", "完成")
                    count += 1
                    exit()
            i += 1
        tkinter.messagebox.showinfo("showinfo", "更新完成")
        exit()
def downloads():
    
    # ------
    import zipfile #zipfile.ZipFile
    if fn == None:
      if len(list(data)) == 0:
        yt_urls = input("enter your file's full url")
      else:
        yt_urls = data
      yt_urls = yt_urls.split(",")
      i = 0
      yt_title = []
      print("wget is on path %s" % (wget.__file__))
      for yt_url in yt_urls:
        
        if yt_url == "":
          yt_url = "https://github.com/sam-teng/update-data/blob/main/pythonGame-autoUpdate/game_socket-client_2P-GUIv2.py"
        try:
          url = yt_url
          r = requests.get(url, auth=('user', 'pass'))#https://api.github.com
          print(r.status_code)
          print(r.headers['content-type'])
          
          response = requests.get(f'{url}')
            
          with open("%d.zip"%(i), 'wb') as file:
              file.write(response.content)
              file.close()
          """
          req = urllib.request(url)
          downloadurl = urllib.urlopen(req)
          zipcontent = downloadurl.read()
          with open("%d.py"%(i), 'wb') as f:#with open("%d."+input("請輸入副檔名")%(i), 'wb') as f:
              f.write(zipcontent)
              """
          """
          w = wget.download(url,out="\\"+str(i)+".zip")
          """
          from zipfile import ZipFile
          
          test_file_name = str(i)+".zip"

          with ZipFile(test_file_name, 'r') as zip:
            zip.printdir()
            zip.extractall("temp") 
          """
          yt = YouTube(yt_url)#YouTube('https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ')
          print('strart downloads: ',yt.title)
          path = ""#yt.title
          #yt_title = yt_title.join(yt.title)
          yt_title.append(yt.title)
          """
          """
          if not os.path.exists(path):
            os.makedirs(path)
          """
          #print(type(yt))
          """
          yt.streams.filter(subtype='mp4').first().download(path)#
          print('finish',yt.title,'downloads!')
          """
          
          #exec(open("cheakfile.py").read())
          
        except:
          print("can't from" + yt_url + "\t download file")
          #yt_title.remove(yt.title)
        finally:
          i = i + 1
          time.sleep(3)
        
    else:
      pass
    loading()
def state():
    global count
    if bytes >= maxbytes:
        count += 1

th1 = threading.Thread(target = downloads())
#load()
th2 = threading.Thread(target = root.mainloop())
#root.mainloop()
th3 = threading.Thread(target = state())
#count += 1
th4 = threading.Thread(target = load())
#cheakstate()

def cheakstate():
    if count == 0:
        pass#count += 1
    elif count == 1:
        tkinter.messagebox.showinfo("showinfo", "更新完成")
        
        time.sleep(1)
        
    elif count == 2:
        time.sleep(1.5)
        th1.join()
        th3.join()
        th4.join()
        #th5.join()
        th2.join()
        #exit()
        
th5 = threading.Thread(target = cheakstate())

#load()
#downloads()
#cheakstate()
th2.start()

th5.start()
th3.start()
th4.start()
th1.start()

