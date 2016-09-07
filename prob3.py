div = 2
leftover = 600851475143
while leftover>1:
    if leftover % div==0:
        leftover = leftover // div
        print(div,'is a divisor',leftover,'left over')
    div += 1
        
        
