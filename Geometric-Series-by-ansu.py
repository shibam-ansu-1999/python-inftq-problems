
n = int(input())

if n%2 == 0:
  n1 = 1
  nth = n1 * (3**(n//2-1))

else:
  n1 = 1
  nth = n1 * (2**(n//2))
  
print(nth)
    
