# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox

import os
import threading

import run
from run import main#,setting

root = Tk()
root.title("Mune")#ch16_8
root.geometry("300x180")
root.iconbitmap('unicorn') # 更改左上角的icon圖示

try:
    basePath = "./"
except:
    basePath = os.getcwd().replace("\\", "/")+"/"

E_count = 0

def _cheakUpdate():
    
    from cheakUpdateV0_4 import __init__
    global E_count
    fileName = "webDownloader-beta2.11.7"
    file_name = "webDoenloader-"
    #file_name.split(".").pop()
    
    #i = 0
    with open(os.path.join(basePath,"config"),"r") as config:
        config = config.read()
        print("config:",config)
        for c in config.split(",\n"):
            #print(file_name,c)
            #i += 1
            if file_name in c:
                #i -= 1
                fileName = c
            
                break
    #print("i:",i)
    
    #if not i == 1:
        #return
    if not os.path.isfile(os.path.join(basePath,fileName+".exe")):
        try:
            exec(open(fileName+".py","rb").read())
            return False
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
            E_count += 1
            print("Can not find the Downloader!")
            tkinter.messagebox.showinfo("ERROR", "更新錯誤")
            return True
    elif not os.path.isfile(os.path.join(basePath,fileName+".py")):
        try:
            os.system(fileName+".exe")
            return False
        except:
            E_count += 1
            print("Can not find the Downloader!")
            tkinter.messagebox.showinfo("ERROR", "更新錯誤")
            return True
    else:
        print("Can not find the Downloader!")
        tkinter.messagebox.showinfo("ERROR", "更新錯誤")
        cheakUpdate()
    if E_count >= 5:
        print("Can not find the Downloader!")
        tkinter.messagebox.showinfo("ERROR", "更新錯誤")
        return False
    
#檢查更新
#while cheakUpdate():
#_cheakUpdate()

"""
fr = ""
with open("webDownloader-beta2.6.py","rb") as fr:
    fr = fr.read()
    #print(fr)
"""
def __init__():
    t = []
    t.append(threading.Thread(target = __main__()))
    t.append(threading.Thread(target = _cheakUpdate()))
    
    for th in range(len(t)):
        t[th].start()
        if th == 0:
            continue
        #while _cheakUpdate():
        t[th].join()
        if th <= len(t):
            th += 1

def _exit():
    run._exit()
    root.destroy()
    exit()

def __main__():
    menubar = Menu(root)                        # 建立最上層功能表
    # 建立功能表類別物件,和將此功能表類別命名File 
    filemenu = Menu(menubar,tearoff=False)
    menubar.add_cascade(label="File",menu=filemenu,underline=0)
    # 在File功能表內建立功能表清單
    updatamenu = Menu(filemenu,tearoff=False)     # 取消分隔線
    filemenu.add_cascade(label="Help",menu=updatamenu,underline=0)
    # 首先在File功能表內建立updata子功能表物件
    updatamenu.add_command(label="cheakUpdata",command=_cheakUpdate,underline=0)
    # 首先在File功能表內建立find子功能表物件
    #findmenu.add_command(label="game_socket-client_2P-GUIv2.1.py",command=game_s_cli_2)
    #findmenu.add_command(label="game_socket-server_2P-GUIv2.1.py",command=game_s_ser_2)

    gamemenu = Menu(menubar,tearoff=False)     # 取消分隔線
    menubar.add_cascade(label="Game",menu=gamemenu)
    gamemenu.add_command(label="game_socket-client_2P-GUIv2.2",command=main("client"))
    gamemenu.add_command(label="game_socket-server_2P-GUIv2.2",command=main("server"))

    # 下列是增加分隔線和建立Exit!指令
    filemenu.add_separator()
    filemenu.add_command(label="Exit!",command=_exit,underline=0)

    root.config(menu=menubar)                   # 顯示功能表物件
    root.mainloop()

if __name__ == '__main__':
    __init__()
