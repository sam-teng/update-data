import os
import time
import wget,sys
import urllib #urllib2.urlopen 

import requests

from tkinter import *
from tkinter.ttk import *
 
root = Tk()
root.title("cheakUpdate")
bytes = 0                           # 設定初值
maxbytes = 10000                    # 假設下載檔案大小 
count = 0

fn = None
data = """
https://github.com/sam-teng/update-data/blob/main/pythonGame-autoUpdate/game_socket-client_2P-GUIv2.py,
https://github.com/sam-teng/update-data/blob/main/pythonGame-autoUpdate/game_socket-server_2P-GUIv2.py,
https://github.com/sam-teng/update-data/blob/main/pythonGame-autoUpdate/view.py
"""

def load():                         # 啟動Prograssbar
    pb["value"] = 0                 # Prograssbar初始值
    pb["maximum"] = maxbytes        # Prograddbar最大值
    loading()
def loading():                      # 模擬下載資料
    global bytes
    bytes += 500                    # 模擬每次下在500bytes
    pb["value"] = bytes             # 設定指針
    if bytes < maxbytes:
        pb.after(50,loading)        # 經過0.05秒繼續執行loading
    global count
    if count == 0:
        count += 1
        downloads()
    else:
        time.sleep(1.5)
        quit()

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
          req = urllib2.Request(url)
          downloadurl = urllib2.urlopen(req)
          zipcontent = downloadurl.read()
          with open("%d.py"%(i), 'wb') as f:#with open("%d."+input("請輸入副檔名")%(i), 'wb') as f:
              f.write(zipcontent)
          #w = wget.download(url,out="\\"+i+".rar")
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
          
          exec(open("cheakfile.py").read())
          
        except:
          print("can't from" + yt_url + "\t download file")
          #yt_title.remove(yt.title)
        finally:
          i = i + 1
          time.sleep(3)
    else:
      pass
    loading()    

pb = Progressbar(root,length=200,mode="indeterminate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["value"] = 0                     # Prograssbar初始值
load()



root.mainloop()