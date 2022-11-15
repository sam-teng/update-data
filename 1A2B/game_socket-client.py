#https://www.itread01.com/article/1510122002.html
#以下為測試版(4)
import os
import random
import time
#from goto import with_goto,_make_code

#@with_goto

low,high = 0,9

ans = ""
ans1_4 = ""
answers = ""
a = 0

password = [0,1,2,3,4,5,6,7,8,9]
#password = ["0","1","2","3","4","5","6","7","8","9"]

i = 0
while i < 4:
    #ans = "".join(ans)
    #print(ans,"aaaaaa")
    #print(i,"i")
    #z = int(random.randint(low, high)) - int(a)
    '''
    print("111")
    print(low,high)
    '''
    z = random.randint(low, high)
    #high = (z - 1)%9
    if i >= 0:
        #print(password)
        ans1_4 = password[z]
        
        ans1_4 = str(ans1_4)
        password.remove(password[z])
        high = high - 1
    #elif i == 1:
        #a = random.randint(0, 1)
        #if not high-low <= 0:
            #if a == 0:
                #print(low,high)
                #ans1_4 = str(random.randint(low, high))
            #elif a == 1:
                #print(low,high)
                #ans1_4 = str(random.randint(int(high + 2), high))
        #elif high-low <= 0:
        i = i + 1
    #ans1_4 = str(z)
    ans = ans1_4 + str(ans)
    #print(ans,"answer")
    answer = list(str(ans))
    #print(answer)
#print(ans)
count = 0
ia = 0
ib =0
a = 0
b = 0
c = 0



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
    print("\n")
    guest = input("請輸入一個四位數字:\n")
    if len(guest) <  4:
        print("請輸入正確的數字")
    elif len(guest) > 4:
        print("請輸入正確的數字")
    
    else:
        for i in list(guest):
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
    count = count + 1
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
print("目前最高分(猜最少次):",count)
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