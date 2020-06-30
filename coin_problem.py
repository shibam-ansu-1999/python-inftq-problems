curency_amount=[1,5]
curency_amount=sorted(curency_amount,reverse=True)
print(curency_amount)

curency_have={}
curency_used={}

for curency in curency_amount:
    curency_used[curency]=0
    curency_have[curency]=int(input("Enter the number of"+" "+str(curency)+" $ coins "))

print(curency_have)
#print(curency_used)

amount=int(input("Enter the amount: "))

while amount>0 and len(curency_have)>0:
    amount=amount-curency_amount[0]
    curency_used[curency_amount[0]]=curency_used[curency_amount[0]]+1
    curency_have[curency_amount[0]]=curency_have[curency_amount[0]]-1
    #print(curency_have)
    #print(curency_used)
    #print(amount)
    if (amount-curency_amount[0])<0 or (curency_have[curency_amount[0]])==0:
        curency_have.pop(curency_amount[0])
        curency_amount.remove(curency_amount[0])


if amount==0:
    print("Successful")
    print(curency_used)
else:
    print(-1)
        
        
        
        
     
    

   
    

