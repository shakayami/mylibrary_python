characteristic=10**9+7
def plus(input1,input2):
    return (input1+input2)%characteristic
def minus(input1,input2):
    return (input1-input2)%characteristic
def times(input1,input2):
    return (input1*input2)%characteristic
def exponen(input1,input2):
    binaryl=list(str(bin(input2))[2:])
    binarysize=len(binaryl)
    binarylist=[int(binaryl[binarysize-1-i]) for i in range(binarysize)]
    modlist=[0 for i in range(binarysize)]
    modlist[0]=input1
    for i in range(1,binarysize):
        modlist[i]=times(modlist[i-1],modlist[i-1])
    answer=1
    for i in range(binarysize):
        if binarylist[i]==1:
            answer=times(answer,modlist[i])
    return answer
def divide(input1,input2):
    return times(input1,exponen(input2,characteristic-2))
