#https://www.itread01.com/article/1510122002.html
# -*- coding: UTF-8 -*-
import socket
import os
import random
import time
import tkinter as tk
from tkinter import *
import tkinter.messagebox as msg # messagebox要另行匯入，否則會出錯。
#from goto import with_goto,_make_code
#@with_goto
window = tk.Tk()
window.title("socket-game-server_2P")
#window.iconbitmap('unicorn.ico') # 更改左上角的icon圖示
state = 0
def setup_game():
    state = 0
    
    # 宣告協議型別
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 繫結本地網絡卡（多網絡卡選擇），埠
    rdn = str(random.randint(0,9))
    for i in range(0,3):
      rdn = rdn + str(random.randint(0,9))
    
    
    result_label.configure(text="port("+str(rdn)+")")
    
    print("port(",rdn,")")
    server.bind(('0.0.0.0', int(rdn)))
    print(server.getsockname())
    #print(server.bind(('localhost',8888)))
    hostname = socket.gethostname()   
    ip = socket.gethostbyname(hostname)
    enter_label.configure(fg='blue', text="Your computer name is "+hostname+",Your ip address is "+ip)
    print("Your computer name is ",hostname,",Your ip address is ",ip)
    state = 1
    res_boolen = False
def prepear():
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
    count = 0
    second = 0

    with open(file, 'w') as ansf:
        ansf.write("正確答案:" + "\t" + "回答次數:" + ",\n")
        ansf.write(str(ans) + "\t\t\t\t")
    ansf.close()
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
        
    def begin():
        prepear()
        range_label = tk.Label(bottom_frame)
        range_label.pack(side=tk.LEFT)
        range_entry = tk.Entry(bottom_frame)
        range_entry.pack(side=tk.RIGHT)
        
        range_label.pack_forget()
        range_entry.pack_forget()
        
        while bool(res_boolen):# == True:
            enter_label.configure(text="遊戲開始")
            print("start")
            #label.begin
            ranges = str(low) + "~" + str(high) + ":"
            range_label.configure(text=ranges)
            print(ranges)
            data = client.recv(1024) # 1024位元組的資料
            #print(low,high)
            res_guest = data.decode()
            #if bool(res_guest) and count > 0:
                #guest = int(input(ranges))
                #guest = random.randint(low, high)
            #guest = random.randint(low, high)
            #elif count == 0:
                #guest = random.randint(low, high)
            #guest = int(input(ranges))
            def yes():
            #if q == "y" or q == "Y" or q == "yes" or q == "Yes":
                guest = range_entry.get()
                
                #qy_btn.pack_forget()
                ans_label.configure(text="答案:"+str(ans))
                
            '''
            def no():
            #elif q == "n" or q == "N" or q == "no" or q == "No":
            '''    
            qy_btn = tk.Button(bottom_frame, text='確定', command=yes)
            qy_btn.pack()
            game_msg = ""
            game_msg = "對方:"+str(guest)+"\n"
            enter_label.configure(text="你:"+str(guest))
            print("你:"+str(guest))
            #if count == 0:
                #client.send(str(ans).encode('utf-8'))
            client.send(str(game_msg).encode('utf-8'))
            
            time.sleep(1)
            #try:
            
            #except:
                #pass

            #print(ans)
            if guest <= high:
                if guest >= low:
                    
                    if guest < ans:
                        low = guest
                        if (high - 1) - (low - 1) == 2:
                            enter_label.configure(text="錯誤,公布答案"+str(ans)+","+str(count+1) + "次")
                            print("錯誤,公布答案",str(ans))
                            print(str(count+1) + "次")
                            game_msg = "錯誤,公布答案"+str(ans)+str(count+1) + "次"
                            client.send(str(game_msg).encode('utf-8'))
                            break
                        
                        enter_label.configure(text="不正確,太小了")
                        print("不正確,太小了")
                        game_msg = "不正確,太小了"
                        client.send(str(game_msg).encode('utf-8'))
                        #ranges = str(low) + "~" + str(high) + ":"
                        #conn.send(ranges.encode('utf-8'))
                        #conn.close()
                        #goto.begin
                    elif guest > ans:
                        high = guest
                        if high - low == 2:
                            enter_label.configure(text="錯誤,公布答案"+str(ans)+","+str(count+1) + "次")
                            print("錯誤,公布答案:",str(ans))
                            print(str(count+1) + "次")
                            game_msg = "錯誤,公布答案"+str(ans)+str(count+1) + "次"
                            client.send(str(game_msg).encode('utf-8'))
                            break
                        
                        enter_label.configure(text="不正確,太大了")
                        print("不正確,太大了")
                        game_msg = "不正確,太大了"
                        client.send(str(game_msg).encode('utf-8'))
                        #ranges = str(low) + "~" + str(high) + ":"
                        #conn.send(ranges.encode('utf-8'))
                        #conn.close()
                        #goto.begin
                    else:
                        enter_label.configure(text="正確,"+str(count+1) + "次")
                        print("正確")
                        print(str(count+1) + "次")
                        
                        game_msg = "正確"+str(count+1) + "次"
                        client.send(str(game_msg).encode('utf-8'))
                        
                        if count+1 == last:
                            enter_label.configure(text="加油,繼續保持")
                            print("加油,繼續保持")
                            game_msg = "加油,繼續保持"
                            client.send(str(game_msg).encode('utf-8'))
                        elif count+1 < last:
                            enter_label.configure(text="有進步")
                            print("有進步")
                            game_msg = "有進步"
                            client.send(str(game_msg).encode('utf-8'))
                            with open(files, 'w') as f:
                                f.write(str(count+1))
                            f.close()
                            """
                            f = open(files, "w")
                            f.write(str(count+1))
                            f.close()
                            """
                        else:
                            enter_label.configure(text="再加油,快破紀錄了")
                            print("再加油,快破紀錄了")
                            game_msg = "再加油,快破紀錄了"
                            client.send(str(game_msg).encode('utf-8'))
                        second = (second + count) + 1
                        
                        enter_label.configure(text="目前最高分(猜最少次):" + str(second))
                        print("目前最高分(猜最少次):" + str(second))
                        game_msg = "目前最高分(猜最少次):" + str(second)
                        client.send(str(game_msg).encode('utf-8'))
                        break
                        
                else:
                    enter_label.configure(text="請輸入正確的數字")
                    print("請輸入正確的數字")
                    continue
                    #goto.begin
            else:
                enter_label.configure(text="請輸入正確的數字")
                print("請輸入正確的數字")
                continue
                #goto.begin
            count = count + 1
            client.send(" ".encode('utf-8'))
            data = client.recv(1024)
            res_msg = data.decode()
            if res_msg == "You lose":
                i = 1
                enter_label.configure(text="Game over")
                print("You lose")
                continue
    
    def wait():
        #print("hi")
        
        calculate_btn.pack_forget()
        
        begin()
        
    continue_btn = tk.Button(window, text="開始遊戲", command=wait)
    continue_btn.pack()   
    #continue_btn.configure(text="開始遊戲", command=begin)
    
    #begin()

top_frame = tk.Frame(window)

# 將元件分為 top/bottom 兩群並加入主視窗
top_frame.pack()

bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)

left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT)
# 建立事件處理函式（event handler），透過元件 command 參數存取
def quitwindow():
    quit()

# 以下為 top 群組
'''
left_button = tk.Button(top_frame, text='Red', fg='red')
# 讓系統自動擺放元件，預設為由上而下（靠左）
left_button.pack(side=tk.LEFT)

middle_button = tk.Button(top_frame, text='Green', fg='green')
middle_button.pack(side=tk.LEFT)

right_button = tk.Button(top_frame, text='Blue', fg='blue')
right_button.pack(side=tk.LEFT)
'''

ans_label = tk.Label(top_frame, text='答案:')
ans_label.pack(side=tk.LEFT)
ans_entry = tk.Entry(top_frame)
ans_entry.pack(side=tk.LEFT)
'''
port_label = tk.Label(top_frame, text='port:')
port_label.pack(side=tk.LEFT)
port_entry = tk.Entry(top_frame)
port_entry.pack(side=tk.LEFT)
ip_label = tk.Label(top_frame, text='ip:')
ip_label.pack(side=tk.LEFT)
ip_entry = tk.Entry(top_frame)
ip_entry.pack(side=tk.LEFT)
'''

result_label = tk.Label(top_frame)
result_label.pack()

enter_label = tk.Label(top_frame)
enter_label.pack()

calculate_btn = tk.Button(window, text='確定', command=prepear)
calculate_btn.pack()



# 以下為 bottom 群組
# bottom_button 綁定 echo_hello 事件處理，點擊該按鈕會印出 hello world :)


bottom_button = tk.Button(bottom_frame, text='離開', fg='black', command=quitwindow)
# 讓系統自動擺放元件（靠下方）
bottom_button.pack(side=tk.BOTTOM)


#========
setup_game()

# 運行主程式
window.mainloop()
