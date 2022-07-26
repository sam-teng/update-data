# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox

import os

from cheakUpdateV0_1 import *
from run import main,setting

root = Tk()
root.title("Mune")#ch16_8
root.geometry("300x180")

menubar = Menu(root)                        # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
# 首先在File功能表內建立find子功能表物件
#findmenu = Menu(filemenu,tearoff=False)     # 取消分隔線
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

#檢查更新
#while cheakUpdate():
cheakUpdate()

root.mainloop()