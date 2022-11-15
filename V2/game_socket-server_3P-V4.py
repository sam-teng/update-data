#https://www.itread01.com/article/1510122002.html
# -*- coding: UTF-8 -*-
import socket
import os
import random
import time
import asyncio
import threading
#from goto import with_goto,_make_code
#@with_goto

low, high = 1, 100
ans = random.randint(low, high)
file = "server-answerdatalog.csv"
count = 0
second = 0


ansf = open(file, "w")
ansf.write("正確答案:" + "\t" + "回答次數:" + ",\n")
ansf.write(str(ans) + "\t\t\t\t")
ansf.close()
# 宣告協議型別
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 繫結本地網絡卡（多網絡卡選擇），埠
rdn = str(random.randint(0,9))
for i in range(0,3):
  rdn = rdn + str(random.randint(0,9))
print(rdn)
server.bind(('0.0.0.0', int(rdn)))
print(server.getsockname())
hostname = socket.gethostname()   
ip = socket.gethostbyname(hostname)
print("Your computer name is ",hostname,",Your ip address is ",ip)
#print(server.bind(('localhost',8888)))
# 監聽埠
server.listen(20) # 監聽
#clinet = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
  
  conn, address = server.accept()
  print("進入等待時間....")
  while True:
    # 接收資料
    data_server = conn.recv(1024)
    def catch_cient(ds=data_server):
        # 接收資料
        ds = conn.recv(1024)
        if not ds:
          print('client is lost...')
          
        res_other = ds.decode()
        print("收到連線....")
        print(res_other)
        return res_other
    
    print("收到連線....")
    # 接收資料
    data_server = conn.recv(1024)
    if not data_server:
      print('client is lost...')
      break
    else:
        res_ip = data_server.decode()#os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
        print("收到連線....")
        print("res_ip",res_ip)
    
    data_server = conn.recv(1024)
    if not data_server:
      print('client is lost...')
      break
    else:
        res_ip2 = data_server.decode()#os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
        print("收到連線....")
        print("res_ip2",res_ip2)
    
    # 接收資料
    data_server = conn.recv(1024)
    if not data_server:
      print('client is lost...')
      break
    res = data_server.decode()#os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
    # 返回結果
    #conn.send(res.encode('utf-8'))
    time.sleep(1)
    res2 = data_server.decode()
    print(res,1)
    print(res2,2)
    #res_other = res
    #while res_other == res_other_two:
    res_other = threading.Thread(target=catch_cient)#, args=data_server)
    res_other_two = threading.Thread(target=catch_cient)#, args=data_server)
    res_other.strat()
    res_other_two.strat()
    res_other.join()
    print(res_other)
    time.sleep(1)
    res_other_two.join()
    print(res_other_two)
    #res = ""
    '''
    while res == res_other:
        res = data_server.decode()
        print(res,2)
        '''
    #res_other_two = res
    '''
    while res_other_two != res:
        data_server = conn.recv(1024)
        if not data_server:
          print('client is lost...')
          break
        res_other_two = data_server.decode()
        print("收到連線2....")
        print(res_other_two)
        '''
    server.send(res_other.encode('utf-8'))
    #conn.close()
    
    time.sleep(1)
    server.send(res_other_two.encode('utf-8'))
    break
  break
#game begin
#
print("正在等待連線....")
msg = res_other#input('>>:')#.strip()

server.send(msg.encode('utf-8'))

time.sleep(1.5)
msg = str(ans)#input('>>:')#.strip()

server.send(msg.encode('utf-8'))
time.sleep(1.5)

while True:
    
    print("已連線")
    msg = '開始遊戲'#input('>>:')#.strip()
    if len(msg) == 0:
        continue
    server.send(msg.encode('utf-8'))
    time.sleep(1.5)
    #client.send(str(ans).encode('utf-8'))
    #ans = 0
    data = conn.recv(1024) # 1024位元組的資料
    
    ans = int(data.decode())
    #print(ans)
    #print(ranges)
    #client.close()
    time.sleep(0.5)
    msg = '1'
    server.send(msg.encode('utf-8'))
    
    data = conn.recv(1024) # 1024位元組的資料
    #ans = int(data.decode())
    res_boolen = data.decode()
    print(bool(res_boolen))
    if bool(res_boolen):
        server.send(" ".encode('utf-8'))
        data = conn.recv(1024) # 1024位元組的資料
        #ans = int(data.decode())
        res_boolen = data.decode()
        if bool(res_boolen):
            
            break
i = 0
guest = random.randint(low, high)

while bool(res_boolen):# == True:
    print("start")
    #label.begin
    ranges = str(low) + "~" + str(high) + ":"
    print(ranges)
    data = conn.recv(1024) # 1024位元組的資料
    #print(low,high)
    res_guest = data.decode()
    if bool(res_guest) and count > 0:
        guest = random.randint(low, high)
    guest = random.randint(low, high)
    #elif count == 0:
        #guest = random.randint(low, high)
    #guest = int(input(ranges))
    game_msg = ""
    game_msg = "電腦:"+str(guest)+"\n"
    print("電腦:"+str(guest))
    #if count == 0:
        #client.send(str(ans).encode('utf-8'))
    server.send(str(game_msg).encode('utf-8'))
    
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
                    server.send(str(game_msg).encode('utf-8'))
                    break
                    
                print("不正確,太小了")
                game_msg = "不正確,太小了"
                server.send(str(game_msg).encode('utf-8'))
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
                    server.send(str(game_msg).encode('utf-8'))
                    break
                
                print("不正確,太大了")
                game_msg = "不正確,太大了"
                server.send(str(game_msg).encode('utf-8'))
                #ranges = str(low) + "~" + str(high) + ":"
                #conn.send(ranges.encode('utf-8'))
                #conn.close()
                #goto.begin
            else:
                print("正確")
                print(str(count+1) + "次")
                
                game_msg = "正確"+str(count+1) + "次"
                server.send(str(game_msg).encode('utf-8'))
                
                if count+1 == last:
                    print("加油,繼續保持")
                    game_msg = "加油,繼續保持"
                    server.send(str(game_msg).encode('utf-8'))
                elif count+1 < last:
                    print("有進步")
                    game_msg = "有進步"
                    server.send(str(game_msg).encode('utf-8'))
                    f = open(files, "w")
                    f.write(str(count+1))
                    f.close()
                else:
                    print("再加油,快破紀錄了")
                    game_msg = "再加油,快破紀錄了"
                    server.send(str(game_msg).encode('utf-8'))
                second = (second + count) + 1
                
                print("目前最高分(猜最少次):" + str(second))
                game_msg = "目前最高分(猜最少次):" + str(second)
                server.send(str(game_msg).encode('utf-8'))
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
    servert.send(" ".encode('utf-8'))
    data = conn.recv(1024)
    res_msg = data.decode()
    if res_msg == "You lose":
        i = 1
        print("You lose")
        continue

if i == 0:
    game_msg = "You lose"
    server.send(str(game_msg).encode('utf-8'))
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
ansf = open(file, "a")
ansf.write(str(count+1) + ",\n")
ansf.close()
