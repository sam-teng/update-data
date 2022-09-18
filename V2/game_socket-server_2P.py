#https://www.itread01.com/article/1510122002.html
# -*- coding: UTF-8 -*-
import socket
import os
import random
import time
#from goto import with_goto,_make_code
#@with_goto

low, high = 1, 100
ans = input("請輸入一個數字")
while int(ans) <= 0 or int(ans) >= 100:
    ans = input("請輸入一個正確的數字")
ans = abs(int(ans))

#ans = random.randint(low, high)
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
# 宣告協議型別
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 繫結本地網絡卡（多網絡卡選擇），埠
rdn = str(random.randint(0,9))
for i in range(0,3):
  rdn = rdn + str(random.randint(0,9))
print("port(",rdn,")")
server.bind(('0.0.0.0', int(rdn)))
print(server.getsockname())
#print(server.bind(('localhost',8888)))
hostname = socket.gethostname()   
ip = socket.gethostbyname(hostname)
print("Your computer name is ",hostname,",Your ip address is ",ip)
# 監聽埠
server.listen(20) # 監聽
#clinet = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
  
  conn, address = server.accept()
  print("進入等待時間....")
  while True:
    
    print("收到連線....")
    # 接收資料
    data_server = conn.recv(1024)
    if not data_server:
      print('client is lost...')
      break
    res_ip = data_server.decode()#os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
    print("收到連線....")
    print(res_ip)
    
    # 接收資料
    data_server = conn.recv(1024)
    if not data_server:
      print('client is lost...')
      break
    res = data_server.decode()#os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
    # 返回結果
    #conn.send(res.encode('utf-8'))
    conn.close()
    res = data_server.decode()
    print(res)
    #time.sleep(1)
    break
  break
#game begin
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((res_ip, int(res))) # 服務端ip和埠
print("正在等待連線....")
msg = str(ans)#input('>>:')#.strip()

client.send(msg.encode('utf-8'))
time.sleep(1.5)

while True:
    
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

while bool(res_boolen):# == True:
    print("start")
    #label.begin
    ranges = str(low) + "~" + str(high) + ":"
    #print(ranges)
    data = client.recv(1024) # 1024位元組的資料
    #print(low,high)
    res_guest = data.decode()
    #if bool(res_guest) and count > 0:
        #guest = int(input(ranges))
        #guest = random.randint(low, high)
    #guest = random.randint(low, high)
    #elif count == 0:
        #guest = random.randint(low, high)
    guest = int(input(ranges))
    game_msg = ""
    game_msg = "對方:"+str(guest)+"\n"
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
                    print("錯誤,公布答案",str(ans))
                    print(str(count+1) + "次")
                    game_msg = "錯誤,公布答案"+str(ans)+str(count+1) + "次"
                    client.send(str(game_msg).encode('utf-8'))
                    break
                    
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
                    print("錯誤,公布答案:",str(ans))
                    print(str(count+1) + "次")
                    game_msg = "錯誤,公布答案"+str(ans)+str(count+1) + "次"
                    client.send(str(game_msg).encode('utf-8'))
                    break
                
                print("不正確,太大了")
                game_msg = "不正確,太大了"
                client.send(str(game_msg).encode('utf-8'))
                #ranges = str(low) + "~" + str(high) + ":"
                #conn.send(ranges.encode('utf-8'))
                #conn.close()
                #goto.begin
            else:
                print("正確")
                print(str(count+1) + "次")
                
                game_msg = "正確"+str(count+1) + "次"
                client.send(str(game_msg).encode('utf-8'))
                
                if count+1 == last:
                    print("加油,繼續保持")
                    game_msg = "加油,繼續保持"
                    client.send(str(game_msg).encode('utf-8'))
                elif count+1 < last:
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
                    print("再加油,快破紀錄了")
                    game_msg = "再加油,快破紀錄了"
                    client.send(str(game_msg).encode('utf-8'))
                second = (second + count) + 1
                
                print("目前最高分(猜最少次):" + str(second))
                game_msg = "目前最高分(猜最少次):" + str(second)
                client.send(str(game_msg).encode('utf-8'))
                break
                
        else:
            print("請輸入正確的數字")
            continue
            #goto.begin
    else:
        print("請輸入正確的數字")
        continue
        #goto.begin
    count = count + 1
    client.send(" ".encode('utf-8'))
    data = client.recv(1024)
    res_msg = data.decode()
    if res_msg == "You lose":
        i = 1
        print("You lose")
        continue

if i == 0:
    game_msg = "You lose"
    client.send(str(game_msg).encode('utf-8'))
time.sleep(3)

if count <= 3:
    print("太神了吧! 有夠厲害!")
    game_msg = "太神了吧! 有夠厲害!"
elif count <= 5:
    print("也算不錯耶")
    game_msg = "也算不錯耶"
elif count <= 10:
    print("老大:幫幫忙,振作點")
    game_msg = "老大:幫幫忙,振作點"
else:    
    print("不會吧  腦袋裝醬糊嗎?")
    game_msg = "不會吧  腦袋裝醬糊嗎?"
with open(files, 'a') as ansf:
    ansf.write(str(count+1) + ",\n")
ansf.close()
"""
ansf = open(file, "a")
ansf.write(str(count+1) + ",\n")
ansf.close()
"""