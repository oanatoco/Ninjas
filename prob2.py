fib = [1,2]
new_elem = 3
while new_elem < 4000000:
    fib.append(new_elem)
    new_elem = fib[len(fib)-1]+fib[len(fib)-2]
print(fib)
print(sum(fib))
print((sum(fib)+1)/2)
