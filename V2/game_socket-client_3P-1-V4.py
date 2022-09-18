#https://www.itread01.com/article/1510122002.html
#以下為測試版(4)
import os
import random
import time
#from goto import with_goto,_make_code

#@with_goto

low, high = 1, 100
#ans = random.randint(low, high)
ans = input("請輸入一個數字")
while int(ans) <= 0 or int(ans) >= 100:
    ans = input("請輸入一個正確的數字")
ans = abs(int(ans))
count = 0
second = 0
#print(ans)

ip_check = 0

file = "client-answerdatalog.csv"
files = "highest.txt"

ip_log = "ip-list"
if not os.path.exists(ip_log):
    last_ip = ""
else:
    f = open(ip_log)
    last_ip = f.read()
    f.close()
    ip_check = 1
    

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
if ip_check == 1:
    print(last_ip)
    q = input("要使用上一個IP位址嗎?(y/n)")
    if q == "y" or q == "Y" or q == "yes" or q == "Yes":
        ip = last_ip
    elif q == "n" or q == "N" or q == "no" or q == "No":
        ip = input("ip=")
        f = open(ip_log,"w")
        f.write(ip)
        f.close()
    else:
        ip = last_ip
else:
    ip = input("ip=")
    f = open(ip_log,"w")
    f.write(ip)
    f.close()
try:
    client.connect((ip, port)) # 服務端ip和埠
except:
    print("請輸入正確的數字")
    client.connect((ip, port)) # 服務端ip和埠
# python3 接收位元組流資料
hostname = socket.gethostname()   
ip = socket.gethostbyname(hostname)
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
    print(data.decode())
    client.close()
    #time.sleep(1)
    break
#game begin

# 監聽埠

while True:
    
    print("進入等待時間....")
    
    data_client = client.recv(1024)
    if not data_client:
      print('client is lost...')
      break
    #res_ans = os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
    res_ans = data_client.decode()
    # 返回結果
    #conn.send(res_ans.encode('utf-8'))
    #res = int(res)
    #print(res)
    
    #print(ans)
    client.send(str(ans).encode('utf-8'))
    ans = int(res_ans)
    #time.sleep(1)
    data_client = client.recv(1024)
    res = data_client.decode()#os.popen("{}".format(data_server.decode())).read() # 將執行命令的結果儲存返回
    # 返回結果
    #conn.send(res_boolen.encode('utf-8'))
    #print(res)
    time.sleep(1)
    data_client = client.recv(1024)
    res_boolen = data_client.decode()
    print(res_boolen)#.split('~'))
    print(bool(res_boolen))
    if bool(res_boolen):
        break
i = 0
while bool(res_boolen):# == 1:
    print("start")
    #label.begin
    msg = '1'
    client.send(msg.encode('utf-8'))
    time.sleep(0.5)
    """
    try:
    """
    data_client = client.recv(1024)
    res_msg = data_client.decode()
    print(res_msg)
    if res_msg == "You lose":
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
    guest = int(input(ranges))
    

    if guest <= high:
        if guest >= low:
            
            if guest < ans:
                low = guest
                if (high - 1) - (low - 1) == 2:
                    print("錯誤,公布答案",str(ans))
                    print(str(count+1) + "次")
                    break
                else:
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
                    print("錯誤,公布答案:",str(ans))
                    print(str(count+1) + "次")
                    break
                else:
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
            #continue
            #goto.begin
    else:
        print("請輸入正確的數字")
        continue
        #goto.begin
    count = count + 1
    msg = '1'
    client.send(msg.encode('utf-8'))
    time.sleep(1.5)
    client.send(" ".encode('utf-8'))

if i == 0:
    msg = 'You lose'
    client.send(msg.encode('utf-8'))
    print("You win")
time.sleep(3)   
   
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

