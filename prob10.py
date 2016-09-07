def primes_below(nummax):
    primes = [2]
    num = 3
    while num<nummax:
        divisible = 0
        for p in primes:
            #print('p=',p)
            if num % p ==0:
                divisible=1
                break
        if divisible==0:
            #print(num)
            primes.append(num)
        num += 1
    #print(primes)
    return primes

primes_below_2m = primes_below(2000000)
print(primes_below_2m[0:100])
print('length is',len(primes_below_2m))
print(sum(primes_below_2m))

