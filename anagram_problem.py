test_case=int(input("Enter Number of Test Case: "))

for i in range(test_case):
    s1=list(input("Enter ther the 1st sting of test case {}: ".format(i+1)))
    s2=list(input("Enter ther the 2nd sting of test case {}: ".format(i+1)))
    
    for j in s1[:]:
        if j in s2:
                s1.remove(j)
                s2.remove(j)
    print(len(s1)+len(s2))    

       


       


        
