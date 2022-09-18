#https://www.itread01.com/article/1510122002.html
#以下為測試版(4)
import os
import random
import time
#from goto import with_goto,_make_code

#@with_goto

#low,high = 0,9

ans = ""
#ans1_4 = ""
answers = ""
#a = 0
ans = input("請輸入一個四位數字")
for i in list(ans):
    if list(ans).count(i) > 1:
        #print("請輸入正確且不重複的數字")
        ans = input("請輸入一個正確且不重複的四位數字")
        break
answer = list(str(ans))
#print(answer)
#print(ans)
count = 0
ia = 0
ib =0
a = 0
b = 0
c = 0

ip_check = 0

file = "client-answerdatalog.csv"
files = "highest.txt"

with open(file, 'w') as ansf:
    ansf.write(ans)
ansf.close()

ip_log = "ip-list"
if not os.path.exists(ip_log):
    last_ip = ""
else:
    with open(ip_log, 'r') as f:
        last_ip = f.read()
    f.close()
    """
    f = open(ip_log)
    last_ip = f.read()
    f.close()
    """
    ip_check = 1
    

if not os.path.exists(files):
    last = float("inf")
else:
    with open(files, 'r') as f:
        last = f.read()
        if not type(last) == int:
            last = float("inf")
        else:
            last = int(last)
    f.close()
    """
    f = open(files)
    last = int(f.read())
    f.close()
    """

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
print("port(",rdn,")")

port = int(input("port="))
if ip_check == 1:
    print(last_ip)
    q = input("要使用上一個IP位址嗎?(y/n)")
    if q == "y" or q == "Y" or q == "yes" or q == "Yes":
        ip = last_ip
    elif q == "n" or q == "N" or q == "no" or q == "No":
        ip = input("ip=")
        with open(ip_log, 'w') as f:
            f.write(ip)
        f.close()
        """
        f = open(ip_log,"w")
        f.write(ip)
        f.close()
        """
else:
    ip = input("ip=")
    with open(ip_log, 'w') as f:
        f.write(ip)
    f.close()
    """
    f = open(ip_log,"w")
    f.write(ip)
    f.close()
    """
try:
    client.connect((ip, port)) # 服務端ip和埠
except:
    print("請輸入正確的數字")
    port = int(input("port="))
    ip = input("ip=")
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
while bool(res_boolen):# == 1:
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
        print("You lose")
        i = 1
        break
    elif res_msg == " ":
        pass#continue
    """
    except:
        continue
        """
    guest = input("請輸入一個四位數字:")
    if len(guest) <  4:
        print("請輸入正確的數字")
    elif len(guest) > 4:
        print("請輸入正確的數字")

    else:
        for ii in list(guest):
            if list(guest).count(i) > 1:
                print("請輸入正確且不重複的數字")
                break
                
        ib = 0
        #print(list(guess)) 
        for x in list(str(ans)):
            #print(x)
            ia = 0
             

            ib = ib + 1
            #print(ib,"ib")
            for y in list(str(guest)):
                #print("\t" + y + "\n")
                ia = ia + 1
                
                if x == y:
                    
                    #print(ia,"ia")
                     
                    if ib == ia:

                        a = a + 1
                        #print(a,"A")
                        break
                    if not ib == ia:
                        b = b + 1
                        #print(b,"B")

                        
                else:
                    #c = c + 1
                    pass
                    #print("C")
    if a == 4:
        break
    elif a > 0 and b == 0:
        print(a,"A")
    elif a == 0 and b > 0:
        print(b,"B")
    elif a == 0 and b == 0:
        print("C")
    else:
        if b == 0:
            print(a,"A")
        else:
            print(a,"A",b,"B")
    '''
    if a == 4:
        pass
        #break
    elif a == 0:
        pass
        #print("C")
    else:
        if b == 0:
            print(a,"A")
        else:
            print(a,"A",b,"B")
    '''
    a = 0
    b = 0
    c = 0

    #goto.begin
    count = count + 1
    msg = '1'
    conn.send(msg.encode('utf-8'))
    time.sleep(1.5)
    conn.send(" ".encode('utf-8'))

if i == 0:
    msg = 'You lose'
    conn.send(msg.encode('utf-8'))
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
with open(files, 'a') as ansf:
    ansf.write(str(count+1) + ",\n")
ansf.close()
"""
ansf = open(file, "a")
ansf.write(str(count+1) + ",\n")
ansf.close()
"""
