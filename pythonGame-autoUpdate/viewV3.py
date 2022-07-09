# ch16_8.py
# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
import os
basePath = "./"

import threading
t = []
def setup():
    for T in range(1000):
        t.append(None)

th = threading.Thread(target = setup())
"""
rlock = th.RLock(1)
semaphore = th.Semaphore(1)
rlock.acquire()
semaphore.acquire()
"""
# 執行該子執行緒
th.start()
th.join()
def cheakUpdate():
    fileName = "webDownloader-beta2.6"
    if not os.path.isfile(os.path.join(basePath,fileName+".exe")):
        try:
            t[1] = threading.Thread(target = exec(open(fileName+".py","rb").read()))
            try:
                
                rlock1 = t[1].RLock()
                semaphore1 = t[1].Semaphore(1)
                rlock1.acquire()
                semaphore1.acquire()
                # 執行該子執行緒
                print(t[1].start())           
            except:
                return
            finally:
                pass
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
            pass
    elif not os.path.isfile(os.path.join(basePath,fileName+".py")):
        try:
            os.system(fileName+".exe")
        except:
            return
    else:
        return
        #cheakUpdate()
def game_s_cli_2():
    #messagebox.showinfo("Find Next","尋找下一筆")
    fileName = "game_socket-client_2P-GUIv2.2"
    if not os.path.isfile(os.path.join(basePath,fileName+".exe")): 
        exec(open(fileName+".py","rb").read())
    else:
        os.system(fileName+".exe")
def game_s_ser_2():
    #messagebox.showinfo("Find Pre","尋找上一筆")
    fileName = "game_socket-server_2P-GUIv2.2"
    if not os.path.isfile(os.path.join(basePath,fileName+".exe")): 
        exec(open(fileName+".py","rb").read())
    else:
        os.system(fileName+".exe")
    
root = Tk()
root.title("Mune")#ch16_8
root.geometry("300x180")

menubar = Menu(root)                        # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
filemenu.add_command(label="cheakUpdate",command=cheakUpdate,underline=0)
# 首先在File功能表內建立find子功能表物件
#findmenu = Menu(filemenu,tearoff=False)     # 取消分隔線
#findmenu.add_command(label="game_socket-client_2P-GUIv2.1.py",command=game_s_cli_2)
#findmenu.add_command(label="game_socket-server_2P-GUIv2.1.py",command=game_s_ser_2)

gamemenu = Menu(menubar,tearoff=False)     # 取消分隔線
menubar.add_cascade(label="Game",menu=gamemenu)
gamemenu.add_command(label="game_socket-client_2P-GUIv2.2",command=game_s_cli_2)
gamemenu.add_command(label="game_socket-server_2P-GUIv2.2",command=game_s_ser_2)

# 下列是增加分隔線和建立Exit!指令
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)

root.config(menu=menubar)                   # 顯示功能表物件

def __init__():
    root.mainloop()
    
t[0] = threading.Thread(target = __init__())

"""
rlock1 = t[0].RLock()
semaphore1 = t[0].Semaphore(1)
rlock1.acquire()
semaphore1.acquire()
"""
# 執行該子執行緒
t[0].start()           
t[0].join()
"""
rlock1.release()
semaphore1.release()
"""










