d1=9
while d1>=1:
    d2=9
    while d2>=0:
        print('working on d1=',d1,'d2=',d2)
        d3=9
        while d3>=0:           
            leftover = int(str(d1)+str(d2)+str(d3)+str(d3)+str(d2)+str(d1))
            #print(leftover0)
            div = 100
            while div<1000:
                if leftover % div==0:
                    remainder = leftover // div
                    print(div,'is a divisor',remainder,'left over')
                    if remainder<1000 and remainder>=100:
                        print(str(d1)+str(d2)+str(d3)+str(d3)+str(d2)+str(d1))
                        print(div,'*',remainder)
                        print(wtf)                          
                div += 1
            print('moving on')
            print('d1=',d1,'d2=',d2,'d3=',d3,'did not meet the criteria')
            d3 = d3- 1
        d2 = d2- 1
    d1 = d1 - 1
   
        
