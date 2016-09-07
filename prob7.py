def prime_nth(n):
    primes = [2]
    counter=1
    num = 3
    while counter<n:
        divisible = 0
        for p in primes:
            #print('p=',p)
            if num % p ==0:
                divisible=1
                break
        if divisible==0:
            #print(num)
            primes.append(num)
            counter += 1
        num += 1
    #print(primes)
    return primes[n-1]

print(prime_nth(5))
print(prime_nth(100))
print(prime_nth(10001))

        
