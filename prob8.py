f=open('p8num.txt','r')
numstr = f.read()
print(numstr)
numstr = numstr.replace('\n','')
print(numstr)

numstrlist = list(numstr)
print(len(numstrlist))

numlist = [int(i) for i in numstrlist]

def product(listvar):
    mult = 1
    for i in listvar:
        mult = mult*i
    return mult
    
counter=0
currmax=1
while counter<987:
    mult = product(numlist[counter:counter+13])
    if mult>currmax:
        currmax=mult
        counter_max=counter
    counter += 1

print(counter_max,currmax)
                

