# -*- coding: UTF-8 -*-
import socket
import os
import random
import time
import tkinter as tk
#import tkinter.messagebox as msg # messagebox要另行匯入，否則會出錯

window = tk.Tk()
#window.title("socket-game-%s_2P"%(mode))
window.iconbitmap('unicorn.ico') # 更改左上角的icon圖示

#global setting_state, main_state, mode

setting_state = False
main_state = False
mode = ""

basePath = "./"
def ctrl_s_cli_2():
    #messagebox.showinfo("Find Next","尋找下一筆")
    """
    fileName = "game_socket-client_2P-GUIv2.2"
    if not os.path.isfile(os.path.join(basePath,fileName+".exe")): 
        exec(open(fileName+".py","rb").read())
    else:
        os.system(fileName+".exe")
    """
    main("client")
    
def ctrl_s_ser_2():
    #messagebox.showinfo("Find Pre","尋找上一筆")
    """
    fileName = "game_socket-server_2P-GUIv2.2"
    if not os.path.isfile(os.path.join(basePath,fileName+".exe")): 
        exec(open(fileName+".py","rb").read())
    else:
        os.system(fileName+".exe")
    """
    main("server")
    
def __main__():
    
    top_frame = tk.Frame(window)
    bottom_frame = tk.Frame(window)

    # 將元件分為 top/bottom 兩群並加入主視窗
    top_frame.pack()
    result_label = tk.Label(top_frame)
    result_label.pack()
    port_label = tk.Label(top_frame, text='port:')
    port_label.pack(side=tk.LEFT)
    port_entry = tk.Entry(top_frame)
    port_entry.pack(side=tk.LEFT)
    ip_label = tk.Label(top_frame, text='ip:')
    ip_label.pack(side=tk.LEFT)
    ip_entry = tk.Entry(top_frame)
    ip_entry.pack(side=tk.LEFT)
    enter_label = tk.Label(window)
    enter_label.pack()

    calculate_btn = tk.Button(window, text='馬上開始連線', command=main)
    calculate_btn.pack()

    # 以下為 bottom 群組
    # bottom_button 綁定 echo_hello 事件處理，點擊該按鈕會印出 hello world :)

    bottom_button = tk.Button(bottom_frame, text='離開', fg='black', command=_exit)
    # 讓系統自動擺放元件（靠下方）
    bottom_button.pack(side=tk.BOTTOM)
    #=======================================
    menubar = tk.Menu(window)                        # 建立最上層功能表
    # 建立功能表類別物件,和將此功能表類別命名File 
    filemenu = tk.Menu(menubar,tearoff=False)
    menubar.add_cascade(label="File",menu=filemenu,underline=0)
    # 在File功能表內建立功能表清單
    updatamenu = tk.Menu(filemenu,tearoff=False)     # 取消分隔線
    filemenu.add_cascade(label="Help",menu=updatamenu,underline=0)
    # 首先在File功能表內建立updata子功能表物件
    #updatamenu.add_command(label="cheakUpdata",command=_cheakUpdate,underline=0)
    # 首先在File功能表內建立find子功能表物件
    #findmenu.add_command(label="game_socket-client_2P-GUIv2.1.py",command=game_s_cli_2)
    #findmenu.add_command(label="game_socket-server_2P-GUIv2.1.py",command=game_s_ser_2)

    gamemenu = tk.Menu(menubar,tearoff=False)     # 取消分隔線
    menubar.add_cascade(label="Game Setting",menu=gamemenu)
    gamemenu.add_command(label="Setting",command=setting,underline=0)
    #gamemenu.add_command(label="game_socket-client_2P-GUIv2.2",command=main("client"))
    #gamemenu.add_command(label="game_socket-server_2P-GUIv2.2",command=main("server"))

    # 下列是增加分隔線和建立Exit!指令
    filemenu.add_separator()
    filemenu.add_command(label="Exit!",command=_exit,underline=0)

    window.config(menu=menubar)                   # 顯示功能表物件

def import_lib(mode):
    #import socket
    #import os
    #import random
    #import time
    #import tkinter as tk
    #import tkinter.messagebox as msg # messagebox要另行匯入，否則會出錯。
    #from goto import with_goto,_make_code
    #@with_goto
    #window = tk.Tk()
    window.title("socket-game-%s_2P"%(mode))
    #window.iconbitmap('unicorn.ico') # 更改左上角的icon圖示
    
    
def setup_game_client():
    pass
    
def cheak_file(filepath,command=""):
    """
    if command != "":
        exec(lambda command)
        """
    del command
    return os.path.exists(filepath)
def save_file(filepath,data):
    with open(filepath, 'w') as f:
        f.write(data)
    f.close()
    return
def read_file(filepath):
    with open(filepath, 'r') as f:
        data = f.read()
    f.close()
    return data

def client():
    
    top_frame = tk.Frame(window)

    # 將元件分為 top/bottom 兩群並加入主視窗
    top_frame.pack()
    result_label = tk.Label(top_frame)
    result_label.pack()
    
    low, high = 1, 100
    ans = random.randint(low, high)
    #ans = ans_entry.get()
    while int(ans) <= 0 or int(ans) >= 100:
        ans = ans_entry.get()
    ans = abs(int(ans))
    count = 0
    second = 0
    #print(ans)

    ip_check = 0

    file = "client-answerdatalog.csv"
    files = "highest.txt"

    ip_log = "ip-list"
    
    
    if not cheak_file(ip_log):
        last_ip = ""
    else:
        last_ip = read_file(ip_log)
        
        """
        f = open(ip_log)
        last_ip = f.read()
        f.close()
        """
        ip_check = 1
        

    if not cheak_file(files):
        last = float("inf")
    else:
        last = read_file(files)
            
        if not type(last) == int:
            last = float("inf")
        else:
            last = int(last)
        
        """
        f = open(files)
        last = int(f.read())
        f.close()
        """
        

    # 客戶端
    # 宣告協議型別,同時生成socket物件
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    rdn = random.randint(0,9)
    #for i in range(0,3):
    rdn1 = random.randint(0,9)
    rdn2 = random.randint(0,9)
    rdn3 = random.randint(0,9)
        #"{}{}".format("rdn",str(i)) = rdn
        
        #print(rdn+str(i))
    rdn = int("{}{}{}{}".format(rdn,rdn1,rdn2,rdn3))
    print("port(",rdn,")")
    result_label.configure(text="port("+str(rdn)+")")
    
    port = port_entry.get()
    if ip_check == 1:
        print(last_ip)
        #q = input("要使用上一個IP位址嗎?(y/n)")
        enter_label.configure(text="要使用上一個IP位址嗎?")
        
        def yes():
        #if q == "y" or q == "Y" or q == "yes" or q == "Yes":
            ip = last_ip
            qy_btn.pack_forget()
            qn_btn.pack_forget()
        def no():
        #elif q == "n" or q == "N" or q == "no" or q == "No":
            ip = ip_entry.get()
            save_file(ip_log,ip)
            
            """
            f = open(ip_log,"w")
            f.write(ip)
            f.close()
            """
            qy_btn.pack_forget()
            qn_btn.pack_forget()
        qy_btn = tk.Button(top_frame, text='確定', command=yes)
        qy_btn.pack()
        qn_btn = tk.Button(top_frame, text='取消', command=no)
        qn_btn.pack()
    else:
        ip = ip_entry.get()
        save_file(ip_log,ip)
        
        """
        f = open(ip_log,"w")
        f.write(ip)
        f.close()
        """
    try:
        client.connect((ip, int(port))) # 服務端ip和埠
    except:
        print("請輸入正確的數字")
        return
        port = port_entry.get()
        ip = ip_entry.get()
        client.connect((ip, int(port))) # 服務端ip和埠
    # python3 接收位元組流資料
    hostname = socket.gethostname()   
    ip = socket.gethostbyname(hostname)
    enter_label.configure(text="Your computer name is "+hostname+",Your ip address is "+ip)
    print("Your computer name is ",hostname,",Your ip address is ",ip)
    msg = ip
    client.send(msg.encode('utf-8'))
    time.sleep(1)
    while True:
        
        msg = str(rdn)#input('>>:')#.strip()
        if len(msg) == 0:
            continue
        client.send(msg.encode('utf-8'))
        data = client.recv(1024) # 1024位元組的資料
        enter_label.configure(text=data.decode())
        print(data.decode())
        client.close()
        #time.sleep(1)
        break
def begin_game_client():
    #game begin
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('0.0.0.0', rdn))
    enter_label.configure(text=server.getsockname())
    print(server.getsockname())
    # 監聽埠
    server.listen(20) # 監聽
    while True:
        conn, address = server.accept()
        enter_label.configure(text="進入等待時間....")
        print("進入等待時間....")
        data_server = conn.recv(1024)
        if not data_server:
          enter_label.configure(text="client is lost...")
          print("client is lost...")
          break
        #res_ans = os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
        res_ans = data_server.decode()
        # 返回結果
        #conn.send(res_ans.encode('utf-8'))
        #res = int(res)
        #print(res)
        
        #print(ans)
        conn.send(str(ans).encode('utf-8'))
        ans = int(res_ans)
        #time.sleep(1)
        data_server = conn.recv(1024)
        res = data_server.decode()#os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
        # 返回結果
        #conn.send(res_boolen.encode('utf-8'))
        #print(res)
        time.sleep(1)
        data_server = conn.recv(1024)
        res_boolen = data_server.decode()
        print(res_boolen)#.split('~'))
        print(bool(res_boolen))
        if bool(res_boolen):
            break
    i = 0
#---------------------------------------------------
state = 0
def setup_game_server():
    state = 0
    
    # 宣告協議型別
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 繫結本地網絡卡（多網絡卡選擇），埠
    rdn = str(random.randint(0,9))
    for i in range(0,3):
      rdn = rdn + str(random.randint(0,9))
    
    top_frame = tk.Frame(window)

    # 將元件分為 top/bottom 兩群並加入主視窗
    top_frame.pack()
    result_label = tk.Label(top_frame)
    result_label.pack()
    
    result_label.configure(text="port("+str(rdn)+")")
    
    print("port(",rdn,")")
    server.bind(('localhost', int(rdn)))
    print(server.getsockname())
    #print(server.bind(('localhost',8888)))
    hostname = socket.gethostname()   
    ip = socket.gethostbyname(hostname)
    enter_label.configure(fg='blue', text="Your computer name is "+hostname+",Your ip address is "+ip)
    print("Your computer name is ",hostname,",Your ip address is ",ip)
    state = 1
    res_boolen = False
    
    low, high = 1, 100
    #ans = random.randint(low, high)
    ans = ans_entry.get()
    
    ans_entry.pack_forget()
    
    if int(ans) <= 0 or int(ans) > 100:
        ans = ans_entry.delete(0,END)
        return
    ans = abs(int(ans))
    count = 0
    second = 0
    #print(ans)

    file = "server-answerdatalog.csv"
    files = "highest.txt"
def server():
    count = 0
    second = 0

    save_file(file, "正確答案:" + "\t" + "回答次數:" + ",\n" + str(ans) + "\t\t\t\t")
    """
        ansf.write("正確答案:" + "\t" + "回答次數:" + ",\n")
        ansf.write(str(ans) + "\t\t\t\t")
    ansf.close()
    """
    """
    ansf = open(file, "w")
    ansf.write("正確答案:" + "\t" + "回答次數:" + ",\n")
    ansf.write(str(ans) + "\t\t\t\t")
    ansf.close()
    """
    if state == 1:
        # 監聽埠
        #server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.listen(20) # 監聽
        #clinet = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        while True:
      
          conn, address = server.accept()
          enter_label.configure(text="進入等待時間....")
          print("進入等待時間....")
          while True:
            enter_label.configure(text="收到連線....")
            print("收到連線....")
            # 接收資料
            data_server = conn.recv(1024)
            if not data_server:
              enter_label.configure(text="client is lost...")
              print("client is lost...")
              break
            res_ip = data_server.decode()#os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
            enter_label.configure(text="收到連線....")
            print("收到連線....")
            print(res_ip)
            
            # 接收資料
            data_server = conn.recv(1024)
            if not data_server:
              enter_label.configure(text="client is lost...")
              print('client is lost...')
              break
            res = data_server.decode()#os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
            # 返回結果
            #conn.send(res.encode('utf-8'))
            conn.close()
            res = data_server.decode()
            enter_label.configure(text=res)
            print(res)
            #time.sleep(1)
            break
          break
def begin_game_server():
    #game begin
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((res_ip, int(res))) # 服務端ip和埠
    enter_label.configure(text="正在等待連線....")
    print("正在等待連線....")
    msg = str(ans)#input('>>:')#.strip()

    client.send(msg.encode('utf-8'))
    time.sleep(1.5)

    while True:
        
        enter_label.configure(text="已連線")
        print("已連線")
        msg = '開始遊戲'#input('>>:')#.strip()
        if len(msg) == 0:
            continue
        client.send(msg.encode('utf-8'))
        time.sleep(1.5)
        #client.send(str(ans).encode('utf-8'))
        #ans = 0
        data = client.recv(1024) # 1024位元組的資料
        
        ans = int(data.decode())
        #print(ans)
        #print(ranges)
        #client.close()
        time.sleep(0.5)
        msg = '1'
        client.send(msg.encode('utf-8'))
        
        data = client.recv(1024) # 1024位元組的資料
        #ans = int(data.decode())
        res_boolen = data.decode()
        print(bool(res_boolen))
        if bool(res_boolen):
            client.send(" ".encode('utf-8'))
            data = client.recv(1024) # 1024位元組的資料
            #ans = int(data.decode())
            res_boolen = data.decode()
            if bool(res_boolen):
                
                break
    i = 0
    #guest = random.randint(low, high)
    
    enter_label.pack_forget()

        
#m = ""
    
class setting:
    m = ""
    #state = False
    #global mode
    #global setting_state
    #mode = m
    varMode = "client"
    var = tk.StringVar()
    #varC = tk.StringVar()
    #varS = tk.StringVar()
    
    client_radiobtn = tk.Radiobutton(window, text='Client',
                                        variable=var,
                                        value="client"#, offvalue=None
                                        ,command=var.set(varMode))
    server_radiobtn = tk.Radiobutton(window, text='Server',
                                        variable=var,
                                        value="server"#, offvalue=None
                                        ,command=var.set(varMode))
    
    def sets(self):
        
        #if self.m is str:
            #self.m = mode
        #print(self.varC.get(),self.varS.get())
        self.m = self.var.get()
        """
        if self.varC.get() == "client":
            self.varS.set(None)
            self.m = "client"
        if self.varS.get() == "server":
            self.varC.set(None)
            self.m = "server"
           """
        """
        elif mode is int:
            if self.varC.get() == 1:
                self.varS.set(0)
                self.m = "client"
            if self.varS.get() == 1:
                self.varC.set(0)
                self.m = "server"
            return self.m
        """
        #self.client_checkbtn.pack_forget()
        #self.server_checkbtn.pack_forget()
        #mode = self.m
        #print(mode)
        window.title("setting:socket-game-%s_2P"%(self.m))
        return self.m
               
    def __init__(self):
        """
        #self.state = setting_state
        if self.state:
            return
        setting_state = True
        """
        
        
        self.client_radiobtn.pack_forget()
        self.client_radiobtn.pack()
        
        
        
        self.server_radiobtn.pack_forget()
        self.server_radiobtn.pack()
        
class main:
    m = ""
    """
    varC = tk.IntVar()
    varS = tk.IntVar()
    def setting(self):
        
        client_checkbtn = tk.Checkbutton(window, text='Client',
                                        variable=self.varC,
                                        onvalue=1, offvalue=0)
                                        #,command=self.sets(""))
        client_checkbtn.pack()
        server_checkbtn = tk.Checkbutton(window, text='Server',
                                        variable=self.varS,
                                        onvalue=1, offvalue=0)
                                        #,command=self.sets(""))
        server_checkbtn.pack()
    """
    def M_client(self):
        #self.m = mode
        #self.m = "client"
        """
        if self.m == "client":
            self.M_client()
        elif self.m == "server":
            self.M_server()
        else:
            pass
        """
        import_lib("client")
        setup_game_client()
        #client function ctrl_s_cli_2()
        client()
        begin_game_client()
    def M_server(self):
        #elf.m = mode
        #self.m = "server"
        """
        if self.m == "client":
            self.M_client()
        elif self.m == "server":
            self.M_server()
        else:
            pass
        """
        import_lib("server")
        setup_game_server()
        #server function ctrl_s_ser_2()
        server()
        begin_game_server()
    def __init__(self):
        """
        mode => "client" & "server" .
        """
        """
        if not mode == None:
            pass
            #__main__()
        else:
            #mode = self.sets(-1)
            #mode = self.m
            if self.varC.get() == "client":
                self.varS.set(None)
                mode = "client"
            if self.varS.get() == "server":
                self.varC.set(None)
                mode = "server"
        print(mode)
        """
        s = setting().sets()
        
        #self.m = setting.m
        mode = s
        print(mode)
        self.m = mode
        if self.m == "client":
            self.M_client()
        elif self.m == "server":
            self.M_server()
        else:
            pass

def _exit():
    global window
    window.destroy()
    if main_state:
        exit()

if __name__ == '__main__':
    window.title("menu:socket-selet")
    __main__()
    window.mainloop()