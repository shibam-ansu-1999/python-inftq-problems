number=int(input("Enter the number to check is it palindrom or not"))

q=number #to copy the input number

reverse_number=0

while number>0:
    extra=number%10
    reverse_number=reverse_number*10+extra
    number=number//10

if q==reverse_number:
    print("wow you choose a palimdrom number")
else:
    print("opps! this is not a palindrom number")
    
    
