def find_pairs_of_numbers(s,n):

    count=0
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            if s[i]+s[j]==n:
                count+=1
    return count
          
    
s=[3, 4, 1, 8, 5, 9, 0, 6]
n=9
print("Number of pairs:",find_pairs_of_numbers(s,n))
        
