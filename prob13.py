f=open('p13num.txt','r')
numstr = f.read()
#print(numstr)
numstrlist = numstr.split('\n')
print(numstrlist[len(numstrlist)-3:len(numstrlist)-1])

#we don't need all 50 digits
numstrlist = [i[0:13] for i in numstrlist]
print(numstrlist[len(numstrlist)-3:len(numstrlist)-1])

numlist = [int(i) for i in numstrlist]

sum_first15 = sum(numlist)
print(sum_first15)
                

