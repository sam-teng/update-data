# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox

import os
import threading

from cheakUpdateV0_1 import *
from run import main,setting

root = Tk()
root.title("Mune")#ch16_8
root.geometry("300x180")
root.iconbitmap('unicorn') # 更改左上角的icon圖示

menubar = Menu(root)                        # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
updatamenu = Menu(filemenu,tearoff=False)     # 取消分隔線
filemenu.add_cascade(label="Help",menu=updatamenu,underline=0)
# 首先在File功能表內建立updata子功能表物件
updatamenu.add_command(label="cheakUpdata",command=cheakUpdate,underline=0)
# 首先在File功能表內建立find子功能表物件
#findmenu.add_command(label="game_socket-client_2P-GUIv2.1.py",command=game_s_cli_2)
#findmenu.add_command(label="game_socket-server_2P-GUIv2.1.py",command=game_s_ser_2)

gamemenu = Menu(menubar,tearoff=False)     # 取消分隔線
menubar.add_cascade(label="Game",menu=gamemenu)
gamemenu.add_command(label="game_socket-client_2P-GUIv2.2",command=main("client"))
gamemenu.add_command(label="game_socket-server_2P-GUIv2.2",command=main("server"))

# 下列是增加分隔線和建立Exit!指令
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)

root.config(menu=menubar)                   # 顯示功能表物件

def _cheakUpdate():
    fileName = "webDownloader-beta2.6"
    if not os.path.isfile(os.path.join(basePath,fileName+".exe")):
        try:
            exec(open(fileName+".py","rb").read())
        except:
            """
            try:
                
                t[1] = threading.Thread(target = r'from fileName import *')
                
                rlock1 = t[1].RLock()
                semaphore1 = t[1].Semaphore(1)
                rlock1.acquire()
                semaphore1.acquire()
                # 執行該子執行緒
                t[1].start()
                t[1].join()
                rlock1.release()
                semaphore1.release()
            except:
                return
            finally:
                pass
            """
            return
    elif not os.path.isfile(os.path.join(basePath,fileName+".py")):
        try:
            os.system(fileName+".exe")
        except:
            return
    else:
        cheakUpdate()

#檢查更新
#while cheakUpdate():
#_cheakUpdate()

"""
fr = ""
with open("webDownloader-beta2.6.py","rb") as fr:
    fr = fr.read()
    #print(fr)
"""
def init():
    t = []
    t.append(threading.Thread(target = root.mainloop()))
    t.append(threading.Thread(target = _cheakUpdate()))
    
    for th in range(len(t)):
        t[th].start()
        t[th].join()
