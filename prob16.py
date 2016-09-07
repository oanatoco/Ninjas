import math

powers2 = []
sum_digits = []
num = 1
for i in range(1,91):
    num = num*2
    powers2.append(num)
    #print('2^',i,'=',num)
    numstr = str(num)
    digits = list(numstr)
    digits = [int(i) for i in digits]
    print('2^',i,'=',digits,'sum is:',sum(digits))
    sum_digits.append(sum(digits))
    sumd = 0
    num5plus = 0
    for d in digits:
        d2 = 2*d
        dig = [int(i) for i in list(str(d2))]
        sumd = sumd + sum(dig)
        if d>=5:
            num5plus += 1
    sumd2 = 2*sum(digits) - 9*num5plus        
    print('predicted next sum from doubling all coefficients:',sumd)
    print(num5plus,'digits 5 and over => predict',sumd2)
    
    
#print(powers2)
print(sum_digits)


