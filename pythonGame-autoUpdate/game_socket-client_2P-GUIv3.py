#def import_lib():
import socket
import os
import random
import time
import tkinter as tk
import tkinter.messagebox as msg # messagebox要另行匯入，否則會出錯。
#from goto import with_goto,_make_code
#@with_goto
window = tk.Tk()
window.title("socket-game-client_2P")
#window.iconbitmap('unicorn.ico') # 更改左上角的icon圖示

file = "client-answerdatalog.csv"
files = "highest.txt"

ip_log = "ip-list"

def setup_game():
    
    low, high = 1, 100
    #ans = random.randint(low, high)
    ans = ans_entry.get()
    while int(ans) <= 0 or int(ans) >= 100:
        ans = ans_entry.get()
    ans = abs(int(ans))
    count = 0
    second = 0
    #print(ans)

    ip_check = 0

def cheak_file(filepath,command=""):
    if command != "":
        exec(lambda:command)
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
    calculate_btn.configure(text="開始遊戲", command=begin)
def begin():
    range_label = tk.Label(bottom_frame)
    range_label.pack(side=tk.LEFT)
    range_entry = tk.Entry(bottom_frame)
    range_entry.pack(side=tk.RIGHT)

    while bool(res_boolen):# == 1:
        enter_label.configure(text="遊戲開始")
        print("start")
        #label.begin
        msg = '1'
        conn.send(msg.encode('utf-8'))
        time.sleep(0.5)
        """
        try:
        """
        data_server = conn.recv(1024)
        res_msg = data_server.decode()
        print(res_msg)
        if res_msg == "You lose":
            enter_label.configure(text="Game over")
            print("You lose")
            i = 1
            break
        elif res_msg == " ":
            pass#continue
        """
        except:
            continue
            """
        ranges = str(low) + "~" + str(high) + ":"
        range_label.configure(text=ranges)
        #guest = int(input(ranges))
        def yes():
        #if q == "y" or q == "Y" or q == "yes" or q == "Yes":
            guest = range_entry.get()
        '''
        def no():
        #elif q == "n" or q == "N" or q == "no" or q == "No":
        '''    
        qy_btn = tk.Button(bottom_frame, text='確定', command=yes)
        qy_btn.pack()

        if guest <= high:
            if guest >= low:
                
                if guest < ans:
                    low = guest
                    if (high - 1) - (low - 1) == 2:
                        enter_label.configure(text="錯誤,公布答案"+str(ans)+","+str(count+1) + "次")
                        print("錯誤,公布答案",str(ans))
                        print(str(count+1) + "次")
                        break
                    else:
                        enter_label.configure(text="不正確,太小了")
                        print("不正確,太小了")
                    #goto.begin
                    #ranges = str(low) + "~" + str(high) + ":"
                    #conn.send(ranges.encode('utf-8'))
                    #conn.close()
                    """
                    msg = '1'
                    conn.send(msg.encode('utf-8'))
                    """
                elif guest > ans:
                    high = guest
                    if high - low == 2:
                        enter_label.configure(text="錯誤,公布答案"+str(ans)+","+str(count+1) + "次")
                        print("錯誤,公布答案:",str(ans))
                        print(str(count+1) + "次")
                        break
                    else:
                        enter_label.configure(text="不正確,太大了")
                        print("不正確,太大了")
                    #goto.begin
                    #ranges = str(low) + "~" + str(high) + ":"
                    #conn.send(ranges.encode('utf-8'))
                    #conn.close()
                    """
                    msg = '1'
                    conn.send(msg.encode('utf-8'))
                    """
                else:
                    enter_label.configure(text="正確,"+str(count+1) + "次")
                    print("正確")
                    print(str(count+1) + "次")
                    
                    if count+1 == last:
                        enter_label.configure(text="加油,繼續保持")
                        print("加油,繼續保持")
                    elif count+1 < last:
                        enter_label.configure(text="有進步")
                        print("有進步")
                        save_file(files,str(count+1))
                        """
                        with open(files, 'w') as f:
                            f.write(str(count+1))
                        f.close()
                        """
                        """
                        f = open(files, "w")
                        f.write(str(count+1))
                        f.close()
                        """
                    else:
                        enter_label.configure(text="再加油,快破紀錄了")
                        print("再加油,快破紀錄了")

                    second = (second + count) + 1
                    enter_label.configure(text="目前最高分(猜最少次):" + str(second))
                    print("目前最高分(猜最少次):" + str(second))
                    break
                    
            else:
                enter_label.configure(text="請輸入正確的數字")
                print("請輸入正確的數字")
                #continue
                #goto.begin
        else:
            enter_label.configure(text="請輸入正確的數字")
            print("請輸入正確的數字")
            continue
            #goto.begin
        count = count + 1
        msg = '1'
        conn.send(msg.encode('utf-8'))
        time.sleep(1.5)
        conn.send(" ".encode('utf-8'))
    
def __init__():
    #import_lib()
    pass

def __main__():
    
    setup_game()
    client()
    #begin_game()
#__init__()
   
top_frame = tk.Frame(window)

# 將元件分為 top/bottom 兩群並加入主視窗
top_frame.pack()

bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)

left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT)
# 建立事件處理函式（event handler），透過元件 command 參數存取
def quitwindow():
    import tkinter as tk
    window = tk.Tk()
    window.destroy()
    exit()

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
port_label = tk.Label(top_frame, text='port:')
port_label.pack(side=tk.LEFT)
port_entry = tk.Entry(top_frame)
port_entry.pack(side=tk.LEFT)
ip_label = tk.Label(top_frame, text='ip:')
ip_label.pack(side=tk.LEFT)
ip_entry = tk.Entry(top_frame)
ip_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

enter_label = tk.Label(window)
enter_label.pack()

calculate_btn = tk.Button(window, text='馬上開始連線', command=__main__)
calculate_btn.pack()

# 以下為 bottom 群組
# bottom_button 綁定 echo_hello 事件處理，點擊該按鈕會印出 hello world :)

bottom_button = tk.Button(bottom_frame, text='離開', fg='black', command=quitwindow)
# 讓系統自動擺放元件（靠下方）
bottom_button.pack(side=tk.BOTTOM)

# 運行主程式
window.mainloop()