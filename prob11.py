f=open('p11num.txt','r')
numstr = f.read()
print(numstr)
numstr_list = numstr.split('\n')
print(numstr_list)
print('number of rows:',len(numstr_list))

matrix = []
for row in numstr_list:
    rowlist = row.split(' ')
    matrix.append(rowlist)

print()
print(len(matrix),'by',len(matrix[0]),'matrix')
for row in range(20):
    for col in range(20):
        matrix[row][col]=int(matrix[row][col])

print(matrix)
currmax=1
for col in range(17):
    for row in range(17):
        prod = matrix[row][col]*matrix[row+1][col+1]*matrix[row+2][col+2]*matrix[row+3][col+3]
        if prod > currmax:
            currmax=prod
            rowmax=row
            colmax=col
            print('Next best is',rowmax,colmax,currmax)
        prod = matrix[row][col]*matrix[row+1][col]*matrix[row+2][col]*matrix[row+3][col]
        if prod > currmax:
            currmax=prod
            rowmax=row
            colmax=col
            print('Next best is',rowmax,colmax,currmax)
        prod = matrix[row][col]*matrix[row][col+1]*matrix[row][col+2]*matrix[row][col+3]
        if prod > currmax:
            currmax=prod
            rowmax=row
            colmax=col
            print('Next best is',rowmax,colmax,currmax)
        prod = matrix[row][col+3]*matrix[row+1][col+2]*matrix[row+2][col+1]*matrix[row+3][col]
        if prod > currmax:
            currmax=prod
            rowmax=row
            colmax=col
            print('Next best is',rowmax,colmax,currmax)
            
print('Final solution',rowmax,colmax,currmax)
