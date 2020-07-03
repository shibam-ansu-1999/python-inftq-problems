import time
def fib(number,d):
    if number in d:
        return d[number]
    else:
        d[number]=fib(number-1,d)+fib(number-2,d)
        return d[number]
    
start_time=time.time()
d={0:1,1:1}
print(fib(53,d))
print("Time taken:",time.time()-start_time)
