import random

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
#print(ans)
count = 0
ia = 0
ib =0
a = 0
b = 0
c = 0



while True:
    
    print("\n")
    guess = input("請輸入一個四位數字:\n")
    if len(guess) <  4:
        print("請輸入正確的數字")
    elif len(guess) > 4:
        print("請輸入正確的數字")
    else:
        
        ib = 0
        #print(list(guess)) 
        for x in list(str(ans)):
            print(x)
            ia = 0
             

            ib = ib + 1
            print(ib,"ib")
            for y in list(str(guess)):
                print("\t" + y + "\n")
                ia = ia + 1
                
                if x == y:
                    
                    print(ia,"ia")
                     
                    if ib == ia:

                        a = a + 1
                        print(a,"A")
                        break
                    if not ib == ia:
                        b = b + 1
                        print(b,"B")

                        
                else:
                    print("C")
            
        if a == 4:
            break
        elif a == 0:
            print("C")
        else:
            if b == 0:
                print(a,"A")
            else:
                print(a,"A",b,"B")
        a = 0
        b = 0
        c = 0
    count = count + 1
print("目前最高分(猜最少次):",count)