#import timeit

#start = timeit.timeit()
print("hello")

nummax = 2000000
primes = [2]
num = 3
while num<nummax:
    divisible = 0
    for p in primes:
        #print('p=',p)
        if num % p ==0:
            divisible=1
            break
        if p>(num**0.5):
            break
    if divisible==0:
        #print(num)
        primes.append(num)
    num += 1
    #print(primes)

print(primes[0:100])
print('looking for primes below',nummax)
print('length is',len(primes))
print(sum(primes))

#end = timeit.timeit()
#print(end - start)

