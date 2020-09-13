import math

def fibo(num):
    n1 = 1
    n2 = 1
    if num == 1 or num == 2:
        print (1)
    else:
        for i in range(2,num):
            tn = n1 + n2
            n1 = n2
            n2= tn
        print (tn)
        

def prime(num):
    
    flag = 0
    count = 0

    for i in range(2,num*100):
        flag = 0 
        x = math.ceil(i/2)
       
        for j in range(2,x+1):

            if i%j == 0:
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            count += 1
        if count == num - 1:
            print(i)
            break
    
num = int(input("Enter the Number to Know the 'n'th term of this special series : "))

if (num%2 == 0):
    execution = math.ceil(num/2)
    prime(execution)
else:
    execution = math.ceil(num/2)
    fibo(execution)
    
