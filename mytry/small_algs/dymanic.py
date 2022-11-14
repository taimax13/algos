def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 
    elif len(array) ==1:
        return array[0]        
    res=array[:]
    res[1]=max(array[0],array[1])
    for i in range(2,len(array)):
        res[i]=max(res[i-1], res[i-2]+array[i])
    return res[-1]

#print(maxSubsetSumNoAdjacent([7,10,12,7,9,14]))       
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 
    elif len(array) ==1:
        return array[0]        
    res=array[:]
    res[1]=max(array[0],array[1])
    for i in range(2,len(array)):
        res[i]=max(res[i-1], res[i-2]+array[i])
    return res[-1]

##############################################################
def numberOfWaysToMakeChange(n, denoms):
    res=[0 for i in range(n+1)]
    res[0]=1
    for denom in denoms:
        for i in range(1, n+1):
            if denom <= i:
                res[i] +=res[i-denom]
    return res[n] 

##############################################################
def minNumberOfCoinsForChange(n, denoms):
    res=[float('inf') for i in range(n+1)]
    res[0]=0
    for denom in denoms:
        for i in range(len(res)):
            if denom <= i:
                res[i] =min(res[i], 1+res[i-denom])
    return res[n] if res[n] !=float('inf') else -1




##############################################################



