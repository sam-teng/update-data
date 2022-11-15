#https://www.itread01.com/article/1510122002.html
#以下為測試版(4)
import os
import random
import time
from goto import with_goto,_make_code

#@with_goto

low, high = 1, 100
ans = random.randint(low, high)
count = 0
second = 0
#print(ans)


file = "answerdatalog.csv"
files = "highest.txt"




if not os.path.exists(files):
    last = float("inf")
else:
    f = open(files)
    last = int(f.read())
    f.close()


# -*- coding: UTF-8 -*-
import socket
import random
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
print(rdn)

port = int(input("port="))
try:
    client.connect(('192.168.1.101', port)) # 服務端ip和埠
except:
    print("請輸入正確的數字")
    client.connect(('192.168.1.101', port)) # 服務端ip和埠
# python3 接收位元組流資料
while True:
    
    msg = str(rdn)#input('>>:')#.strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024) # 1024位元組的資料
    print(data.decode())
    client.close()
    #time.sleep(1)
    break
#game begin
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0', rdn))
print(server.getsockname())
# 監聽埠
server.listen(20) # 監聽
while True:
    conn, address = server.accept()
    print("進入等待時間....")
    data_server = conn.recv(1024)
    if not data_server:
      print('client is lost...')
      break
    res = os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
    res = data_server.decode()
    # 返回結果
    conn.send(res.encode('utf-8'))
    #res = int(res)
    #print(res)
    
    conn.send(str(ans).encode('utf-8'))
    ans = int(res)
    #time.sleep(1)
    data_server = conn.recv(1024)
    res = data_server.decode()#os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
    # 返回結果
    #conn.send(res_boolen.encode('utf-8'))
    print(res)
    time.sleep(1)
    data_server = conn.recv(1024)
    res_boolen = data_server.decode()
    print(res_boolen)#.split('~'))
    print(bool(res_boolen))

    break
while bool(res_boolen):# == 1:
    print("start")
    #label.begin
    ranges = str(low) + "~" + str(high) + ":"
    guest = int(input(ranges))
    
    

    if guest <= high:
        if guest >= low:
            
            if guest < ans:
                low = guest
                if (high - 1) - (low - 1) == 2:
                    print("錯誤,公布答案",str(ans))
                    print(str(count+1) + "次")
                    break
                    
                print("不正確,太小了")
                #goto.begin
                #ranges = str(low) + "~" + str(high) + ":"
                #conn.send(ranges.encode('utf-8'))
                #conn.close()
                msg = '1'
                conn.send(msg.encode('utf-8'))
            elif guest > ans:
                high = guest
                if high - low == 2:
                    print("錯誤,公布答案:",str(ans))
                    print(str(count+1) + "次")
                    break
                
                print("不正確,太大了")
                #goto.begin
                #ranges = str(low) + "~" + str(high) + ":"
                #conn.send(ranges.encode('utf-8'))
                #conn.close()
                msg = '1'
                conn.send(msg.encode('utf-8'))
            else:
                print("正確")
                print(str(count+1) + "次")
                
                if count+1 == last:
                    print("加油,繼續保持")
                elif count+1 < last:
                    print("有進步")
                    f = open(files, "w")
                    f.write(str(count+1))
                    f.close()
                else:
                    print("再加油,快破紀錄了")

                second = (second + count) + 1
                
                print("目前最高分(猜最少次):" + str(second))
                break
                
        else:
            print("請輸入正確的數字")
            #goto.begin
    else:
        print("請輸入正確的數字")
        #goto.begin
    count = count + 1

if count <= 3:
    print("太神了吧! 有夠厲害!")
elif count <= 5:
    print("也算不錯耶")
elif count <= 10:
    print("老大:幫幫忙,振作點")
else:    
    print("不會吧  腦袋裝醬糊嗎?")
ansf = open(file, "a")
ansf.write(str(count+1) + ",\n")
ansf.close()