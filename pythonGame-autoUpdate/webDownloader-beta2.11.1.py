import os,site
import time
import wget,sys
#import urllib #urllib2.urlopen

if sys.version_info >= (3, 0):
    import urllib
else:
    # Import urllib2 to catch errors
    import urllib2

import requests

import threading

from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox

from cheakfileV1_5 import * #cheakFile,replaceFile

root = Tk()
root.title("cheakUpdate")
with open("unicorn", "rb") as ico:
    with open("unicorn.ico", "wb") as icof:
        icof.write(ico.read())
try:
    root.iconbitmap('unicorn.ico') # 更改左上角的icon圖示
except IOError as e:
    try:
        root.iconbitmap('unicorn') # 更改左上角的icon圖示
    except FileError as e:
        print("Can not find the icon")

_bytes = 0                          # 設定初值
maxbytes = 10000                    # 假設下載檔案大小
state = 0
count = 0
i = 0
lenght = 0

th = []
t = []

fn = None
data = """\
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
    rl = threading.RLock()
    sem = threading.Semaphore(2)
    rl.acquire()
    sem.acquire()
    root.mainloop()
    rl.release()
    sem.release()

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)#mode="indeterminate"
pb.pack(padx=10,pady=10)
#pb["value"] = 0                     # Prograssbar初始值
#pb["maximum"] = maxbytes            # Prograddbar最大值

def load():                         # 啟動Prograssbar
    """
    pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)#mode="indeterminate"
    pb.pack(padx=10,pady=10)
    """
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
        _bytes += maxbytes//lenght   # 模擬每次下載500bytes
        pb["value"] = _bytes              # 設定指針
        return False
        #pb.after(50,loading)        # 經過0.05秒繼續執行loading
    else:
        packageFile(mode="path").main()
        #cleanFile()
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
    maxbytes = lenght
    
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
                print(response)
                

                '''
                file_size = os.path.getsize(response.content) 
                print('File Size:', file_size, 'bytes')
                
                #time.sleep(0.5)
                
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
                """
                with open(""+file_r_path, "rb") as f:
                    my_bytes = f.read()
                    """
                my_bytes = response.content
                    """
                if bool(input("continue bin bytes?")):
                #試試看:跟剛才的版本,看到的my_bytes前一百項,有什麼不同?
                """
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
                """
                    """ 
                   ''' 
                pw = ""
                with open("%d"%(i), 'wb') as file:
                    #th4.start()
                    pw = id(file)
                    file.write(response.content)
                    file.close()
                
                import random
                pw = bytes((str(pw) + str(pw+random.randint(-pw,pw))).encode("UTF-8"))
                
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
                
                test_file_name = str(i)#+".zip"
                
                with ZipFile(test_file_name, 'a') as zip:
                    zip.setpassword(pw)
                    zip.printdir()

                with ZipFile(test_file_name, 'r') as zip:
                    zip.printdir()
                    zip.extractall("temp",pwd = pw) 
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
                
            except InternetError as e:
                print(e,"can't from " + yt_url + "\t download file")
                tkinter.messagebox.showinfo("showinfo", "第"+str(i+1)+"項"+"更新失敗")
                if i+1 == lenght:
                  root.destroy()
                  exit()
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
        """
        #th.join()
        #th0.join()
        th1.join()
        th3.join()
        th4.join()
        #th5.join()
        th2.join()
        """
    
        for ths in range(len(th)):
            th[ths].join()
        exit()
     
def __init__():
    t = [main(),state(),preview(),load(),downloads(),cheakstate()]
    """
    th = threading.Thread(target = preview())
    #th0 = threading.Thread(target = _exec())
    th1 = threading.Thread(target = downloads())
    #load()
    th2 = threading.Thread(target = main())
    #root.mainloop()
    th3 = threading.Thread(target = state())
    #count += 1
    th4 = threading.Thread(target = load())
    #cheakstate()

    th5 = threading.Thread(target = cheakstate())
    """
    ths = 0
    
    for ts in t:
        th.append(threading.Thread(target = ts))
        th[ths].start()
        ths += 1
    """
#load()
#downloads()
#cheakstate()
    th2.start()

    th3.start()
    th.start()
    th.join()
    th4.start()#->move into downloads.
    th1.start()
    #th0.start()
    th5.start()
    """

tkinter.messagebox.showinfo("showinfo", "更新中請耐心等候")

t = [state(),preview(),load(),downloads(),cheakstate(),main()]
__init__()