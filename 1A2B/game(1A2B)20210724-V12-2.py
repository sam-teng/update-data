import random
from 海龜模組 import *
回出發點()
設定方向(0)
速度('normal')
#隱藏游標()
#視窗設定(400, 600)
背景顏色(0,0,0)
畫筆顏色('white')
字型 = ('標楷體',15,'normal')

'''
low,high = 0000,9999
ans = str(random.randrange(low, high,4))
print("\n")
if len(ans) < 2:
    ans = "0"*3 + ans
elif len(ans) < 3:
    ans = "0"*2 + ans
elif len(ans) < 4:
    ans = "0" + ans
print(list(str(ans)))
'''
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



while True:
    print("\n")
    #guest = input("請輸入一個四位數字:\n")
    guest = 輸入文字('提示','請輸入一個四位數字:\n')
    筆跡清除()
    if len(guest) <  4:
        寫字('請輸入正確的數字', align='center', font=字型)
        print("請輸入正確的數字")
    elif len(guest) > 4:
        寫字('請輸入正確的數字', align='center', font=字型)
        print("請輸入正確的數字")
    
    else:
        try:
            _guest = int(guest)
        except:
            continue
        state = True
        for i in list(guest):
            if list(guest).count(i) > 1:
                寫字('請輸入正確且不重複的數字', align='center', font=字型)
                print("請輸入正確且不重複的數字")
                #continue
                state = False
                break
                
        if not state:
            continue
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
            寫字('%dA'%(a), align='center', font=字型)
            print(a,"A")
        elif a == 0 and b > 0:
            寫字('%dB'%(b), align='center', font=字型)
            print(b,"B")
        elif a == 0 and b == 0:
            寫字('C', align='center', font=字型)
            print("C")
        else:
            if b == 0:
                寫字('%dA'%(a), align='center', font=字型)
                print(a,"A")
            else:
                寫字('%dA%dB'%(a,b), align='center', font=字型)
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
    #背景顏色(0,0,0)
    
寫字('目前最高分(猜最少次):', align='center', font=字型)
print("目前最高分(猜最少次):",count)
完成()