import re


def arrayOfProduct(array):
    arr_res=[]
    arr_test=array
    for item in array:
        arr_test.remove(item)
        res=1
        for i in range(len(arr_test)):
            res*=arr_test[i]
        arr_res.append(res) 
        arr_test.insert(0,item)   
    return arr_res

#print(arrayOfProduct([5,1,4,2]))
################################################################
def firstDuplicate(array):
    hash={}
    for i in range(len(array)):
        if array[i] in hash.keys():
            return hash[array[i]]
        else: hash[array[i]]=array[i]
    return -1  
#print(firstDuplicate([2,1,5,2,3,3,4]))    
################################################################
def mergeOverlap(intervals):
    #intervals.sort()
    intervals = sorted(intervals, key=lambda x:x[0])
    res=[]
    currentInt = intervals[0]
    res.append(currentInt) 
    for nextInt in intervals:
        _, currentIntEnd = currentInt
        nextIntStart, nextIntEnd = nextInt

        if currentIntEnd>= nextIntStart:
            currentInt[1] = max(currentIntEnd, nextIntEnd)
        else: 
            currentInt = nextInt
            res.append(currentInt)


    return res    
# print(mergeOverlap([
#     [2, 3],
#     [4, 5],
#     [6, 7],
#     [8, 9],
#     [1, 10]
#   ]))            

########################################################################
def fourNumSum(array, targetSum):
    pairs = {}
    fourSum = []

    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            curSumm = array[i] + array[j]
            diff = targetSum - curSumm
            if diff in pairs:
                for pair in pairs[diff]:
                    fourSum.append(pair + [array[i], array[j]])     
        for k in range(0, i):
            curSumm = array[i] + array[k]
            if curSumm not in pairs:
                pairs[curSumm] = [[array[k], array[i]]]
            else: 
                pairs[curSumm].append([array[k], array[i]])
    return fourSum        
#print(fourNumSum([7,6,4,-1,1,2], 16))  

        #050-934-78-77
############################################################################
def subArraySort(array):
    min_unsorted=float("inf")
    max_unsorted=float("-inf")
    for i in range(len(array)):
        num=array[i]
        if isOutOfPlace(i,num, array):
            min_unsorted=min(array[i], min_unsorted)
            max_unsorted=max(array[i], max_unsorted)

    if min_unsorted == float("inf"):
        return [-1,-1]
    subArrayLeftInd = 0
    while min_unsorted >=array[subArrayLeftInd]:
        subArrayLeftInd+=1  
    subArrayRightInd = len(array)-1 
    while max_unsorted <= array[subArrayRightInd]:
        subArrayRightInd-=1

    return [subArrayLeftInd,subArrayRightInd]        

def isOutOfPlace(i,num, array):
    if i==0:
        return num > array[i+1]
    if i ==  len(array)-1:
        return num < array[i-1]
    return num > array[i+1] or num < array[i-1]    


#print(subArraySort([1,2,4,7,10,11,7,12,6,7,16,18,19]))
##############################################################
def largestRange(array):
    res=[]
    longestLength=0
    hash_range={}
    for item in array: 
        hash_range[item]=True
    for item in array:
        if not item in hash_range.keys():
            continue
        hash_range[item]=False
        currentLength = 1
        left = item-1
        right = item+1
        while left in hash_range:
            hash_range[left]=False
            currentLength +=1
            left -=1
        while right in hash_range:
            hash_range[right]=False
            currentLength +=1
            right +=1    

        if currentLength>longestLength:
            longestLength = currentLength
            res = [left+1, right-1]
    return res

#print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))   
# ###############################################################
# kedaynes algorithm
def sumSubArray(array):
    maxRes, currMax=array[0]
    for i in range(1,len(array)-1):
        maxRes = max(array[i], maxRes+array[i])
        currMax = max(currMax, maxRes)
    return currMax    

#################################################################
def listRewards(array):
    res=[1 for _ in array]
    for i in range(1,len(array)):
        if array[i] > array[i-1]:
            res[i]=(res[i-1]+1)  
        print(res)  
    for i in reversed(range(len(array)-1)):
        if array[i]>array[i+1]:
            res[i]=(max(res[i], res[i+1]+1))
        print(res)
    return sum(res)
#print(listRewards([8,4,2,1,3,6,7,9,5]))  
# ###############################################################
      




 








  