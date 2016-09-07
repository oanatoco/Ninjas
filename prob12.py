nummax = 251
num = []
num.append(1)
num.append(3)
n = 1
num_div = 2
while num_div<nummax:
    n += 1
    num_div = 0
    new_num = int((n+1)*(n+2)/2)
    num.append(new_num)
    sqrt_num = int(num[n]**0.5)
    for p in range(1,sqrt_num):
        #print('p=',p)
        if new_num % p ==0:
            num_div += 1
    #print(num_div)        
    
print(num_div)
print(num[len(num)-1])

