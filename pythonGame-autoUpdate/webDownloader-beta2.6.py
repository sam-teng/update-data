import os,site
import time
import wget,sys
import urllib #urllib2.urlopen 

import requests

import threading

from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox

from cheakfileV1_4_4 import cheakFile,replaceFile

root = Tk()
root.title("cheakUpdate")
_bytes = 0                          # 設定初值
maxbytes = 10000                    # 假設下載檔案大小
state = 0
count = 0
i = 0
lenght = 0

fn = None
data = """
https://github.com/sam-teng/update-data/archive/refs/heads/main.zip,
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
def main():
    root.mainloop()

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)#mode="indeterminate"
pb.pack(padx=10,pady=10)
#pb["value"] = 0                     # Prograssbar初始值
#pb["maximum"] = maxbytes            # Prograddbar最大值

def load():                         # 啟動Prograssbar
    pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)#mode="indeterminate"
    pb.pack(padx=10,pady=10)
    pb["value"] = 0                 # Prograssbar初始值
    pb["maximum"] = maxbytes        # Prograddbar最大值
    
    loading()

def loading():                      # 模擬下載資料
    
    if state == 0:
        
        """
        pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)#mode="indeterminate"
        pb.pack(padx=10,pady=10)
        """
        pb["value"] = 0                 # Prograssbar初始值
        pb["maximum"] = maxbytes        # Prograddbar最大值
        
    global _bytes
    
    
    if _bytes < maxbytes:
        _bytes += 200//len(data.split(","))   # 模擬每次下載500bytes
        pb["value"] = _bytes              # 設定指針
        return False
        #pb.after(50,loading)        # 經過0.05秒繼續執行loading
    else:
        replaceFile().replace_file()
        tkinter.messagebox.showinfo("showinfo", "更新完成")
        #root.destroy()
        return True
        exit()
def preview():
    global lenght
    i = 0
    if fn == None:
        if len(list(data)) == 0:
            yt_urls = input("enter your file's full url")
        else:
            yt_urls = data
        yt_urls = yt_urls.split(",")
        for yt_url in yt_urls:
            i += 1
            if yt_url == "":
              yt_url = "https://github.com/sam-teng/update-data/blob/main/pythonGame-autoUpdate/game_socket-client_2P-GUIv2.py"
            if not "http" in yt_url:
                lenght += 1
                continue
    lenght = i - lenght
def downloads():
    global i
    global lenght
    # ------
    import zipfile #zipfile.ZipFile
    if fn == None:
      if len(list(data)) == 0:
        yt_urls = input("enter your file's full url")
      else:
        yt_urls = data
      yt_urls = yt_urls.split(",")
      #i = 0
      yt_title = []
      print("wget is on path %s" % (wget.__file__))
      for yt_url in yt_urls:
        
        if yt_url == "":
            #yt_url = "https://github.com/sam-teng/update-data/blob/main/pythonGame-autoUpdate/game_socket-client_2P-GUIv2.py"
            continue
        if not "http" in yt_url:
            continue
        try:
          url = yt_url
          r = requests.get(url, auth=('user', 'pass'))#https://api.github.com
          print(r.status_code)
          print(r.headers['content-type'])
          
          response = requests.get(f'{url}')
            
          with open("%d.zip"%(i), 'wb') as file:
              th4.start()
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
          tkinter.messagebox.showinfo("showinfo", "第"+str(i+1)+"項"+"更新失敗")
          if i+1 == lenght:
              root.destroy()
              quit()
          #yt_title.remove(yt.title)
        finally:
          i = i + 1
          time.sleep(3)
        
    else:
      pass
    if not loading():
        downloads()
    else:
        exit()
        pass
        #root.destroy()
def state():
    global count
    if _bytes >= maxbytes:
        count += 1

def cheakstate():
    if count == 0:
        pass#count += 1
    elif count == 1:
        tkinter.messagebox.showinfo("showinfo", "更新完成")
        
        time.sleep(1)
        
    elif count == 2:
        
        time.sleep(1.5)
        #th.join()
        #th0.join()
        th1.join()
        th3.join()
        th4.join()
        #th5.join()
        th2.join()
        exit()
     
def __init__():
    th = threading.Thread(target = preview())
    #th0 = threading.Thread(target = _exec())
    th1 = threading.Thread(target = downloads())
    #load()
    th2 = threading.Thread(target = main())
    #root.mainloop()
    th3 = threading.Thread(target = state())
    #count += 1
    th4 = threading.Thread(target = loading())
    #cheakstate()

    th5 = threading.Thread(target = cheakstate())

#load()
#downloads()
#cheakstate()
    th2.start()

    th5.start()
    th3.start()
    th.start()
    th.join()
    #th4.start()#->move into downloads.
    th1.start()
    #th0.start()
__init__()