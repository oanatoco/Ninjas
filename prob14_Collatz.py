def Collatz(num):
    numlist=[num]
    while num>1:
        if num%2==0:
            num = int(num/2)
        else:
            num = 3*num+1
        #print(num)
        numlist.append(num)
    return numlist

## First, program that returns the Collatz sequence for different starting points
b=True
while b:
    inputstr = input('enter starting number or q to exit: ')

    try:
        startnum = int(inputstr)
        seq = Collatz(startnum)
        print('The Collatz sequence starting at',startnum,'has',len(seq),'elements:')
        invseq=[seq[len(seq)-1-i] for i in range(len(seq))]
        print(invseq)
    except:
        if inputstr=='q':
            print('Exiting this section')
            b=False
        else:
            print('Need integer!')
    print()


b=True
while b:
    inputstr = input('enter max number allowed or q to exit: ')

    try:
        maxnum = int(inputstr)

        maxlength = 2
        for startnum in range(2,maxnum):
            seq = Collatz(startnum)
            if len(seq)>maxlength:
                maxlength = len(seq)
                maxseq = seq
                maxstart = startnum
            startnum += 1
            
        print('Of numbers up to',maxnum,'the Collatz sequence starting at',maxstart,'is the longest with',len(seq),'elements:')
        invseq=[maxseq[len(maxseq)-1-i] for i in range(len(maxseq))]
        print(invseq)
    except:
        if inputstr=='q':
            print('Exiting program')
            b=False
        else:
            print('Need integer!')
    print()
