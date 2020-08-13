leap_year=list()

year=int(input("Enter the starting year[yyyy]: "))

if year%4==0 or (year%400==0 and year%100!=0):
    for i in range(0,15):
        leap_year.append(year+4*i)

else:
    for i in range(1,3):
        year+=1
        if year%4==0 or (year%400==0 and year%100!=0):
            for i in range(0,15):
                leap_year.append(year+4*i)
            break
                       
print(leap_year)
        
    
     
    
       

        
    

