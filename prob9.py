a = 1
while a<500:
    b = 1000*(1000-2*a)/(2000-2*a)
    if b>0 and b % 1 ==0:
        c=1000-a-b
        print(a,b,c)
        break
    a += 1
print(a*b*c)


