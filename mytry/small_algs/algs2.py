from re import A


def minNoChange(array):
    sum=1
    sortedArray=sorted(array)
    print(sortedArray)
    if len(array) == 0 or len(array) == 1:
        return 1
    for i in range(len(sortedArray)):
        if sum<sortedArray[i]:
            return sum
        sum+=sortedArray[i]
    return sum    


#print(minNoChange([1]))

################################################################
##[12,-6,-6] 
def threeNumberSum(array, targetSum):
    res=[]
    res_comb=[]
    sum=0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            for k in range(j+1,len(array)):
                res_comb.append([array[i],array[j],array[k]])
    for item in res_comb:
        sum=0
        for i in item:
            sum+=i
        if sum==targetSum:
            item.sort()
            res.append(item)
            res.sort()      
    return res             
#print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6],0))

################################################################
def smallestDifference(arrayOne, arrayTwo):
   pairs=[]
   map={}
   for i in range(0, len(arrayOne)):
    for j in range(0, len(arrayTwo)):
        pairs.append([arrayOne[i],arrayTwo[j]])    
   for pair in pairs:
    map[abs(pair[0]-pair[1])]=pair
   return map.get(min(map.keys()))
#print(smallestDifference([1,2,3], [5,9,20]))        
#################
def shiftLeft(array, number):
    for item in array:
        if item==number:
            array.remove(number)
            array.append(number)
    return array
#print(shiftLeft([1,2,3,44,44,44,56,44,67,88], 44))            
#######################################
def monotonicArray(array):
    if len(array)==0 or len(array)==1:
        return True
    el0 = array[0]
    countIncrease=0
    countDecrease=0
    countNutral=0
    for element in array:
        if element < el0:
            el0 = element
            countDecrease +=1
        elif element > el0:
            el0 = element
            countIncrease +=1
        elif element==el0:
            countNutral +=1
    if countDecrease+countNutral == len(array) or countIncrease+countNutral == len(array):
        return True        
    return False
#print(monotonicArray([1,2])) 
# ################
def spiralTraverse(array):
    res = []
    if (len(array) == 0):
        return res
 
    m = len(array)
    n = len(array[0])
    seen = [[0 for i in range(n)] for j in range(m)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x = 0
    y = 0
    di = 0
    for i in range(m * n):
        res.append(array[x][y])
        seen[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]
        if (0 <= cr and cr < m and 0 <= cc and cc < n and not(seen[cr][cc])):
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]
    return res    
#print(spiralTraverse([[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7],]))  
# 
# #################################
def spiralTraverse2(array):
    res=[]
    startRow, endRow =0, len(array)-1
    startCol, endCol = 0 , len(array[0]) -1
    while startRow <= endRow and startCol <= endRow:
        for col in range(startCol, endCol + 1):
            res.append(array[startRow][col])

        for row in range(startRow+1 , endRow +1):
            res.append(array[row][endCol])

        for col in reversed(range(startCol,endCol)):
            res.append(array[endRow][col])

        for row in reversed(range(startRow+1, endRow)):
            res.append(array[row][startCol])
        startRow +=1
        endRow-=1
        startCol+=1
        endCol -=1
    return res     
#print(spiralTraverse2([[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7],]))            

################################################################
def spiralTraverseRecursive(array):
    res = []
    spirRecursive(array,0, len(array)-1, 0,len(array[0])-1, res)
    return res

def spirRecursive(array, startRow, startCol, endRow, endCol, res):
    if startRow > endRow or startCol > endCol:
        return 

    for col in range(startCol, endCol + 1):
            res.append(array[startRow][col])

    for row in range(startRow+1 , endRow +1):
            res.append(array[row][endCol])

    for col in reversed(range(startCol,endCol)):
            res.append(array[endRow][col])

    for row in reversed(range(startRow+1, endRow)):
            res.append(array[row][startCol])
    spirRecursive(array, startRow+1, endRow-1,startCol+1, endCol-1, res)        
#print(spiralTraverseRecursive([[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7],])) 
# ################
def strongestPick(array):
    if len(array)<3:
        return 
    picks=[]
    map_peak_len = {}
    for i in range(1,len(array)-1):
        if array[i]>array[i-1] and array[i+1]<array[i]:
            picks.append(i)  
    if len(array)==3 and len(picks)==1:
        return len(array)      
    for item in picks:
        elemnts=[]
        #ind_mid = array[item]
        elemnts.append(array[item])
        for i in reversed(range(1, item+1)):
            if array[i]>array[i-1]:
                elemnts.append(array[i-1])
            else:
                break    
        for i in range(item, len(array)-1):
            if array[i]>array[i+1]:
                elemnts.append(array[i+1])
            else:
                break    
        map_peak_len[array[item]]=len(elemnts)
    list_res=list(map_peak_len.values())
    if list_res==[]: return 0    
    return max(list_res)   
#print(strongestPick([1, 2, 3, 4, 5, 1]))                    
#print(strongestPick([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))  
#print(strongestPick([5, 4, 3, 2, 1, 2, 1]))          
#def strongestPick(array):

#####################################
def zigzagTraverse(array):
    w = len(array[0])-1
    h = len(array)-1
    res=[]
    cc=0
    cr=0
    down=True
    while not outOfBounds(cc,cr,h,w):
        res.append(array[cr][cc])
        if down:
            if cc == 0 or cr==h:
                down=False
                if cr == h:
                    cc+=1
                else:
                    cr+=1    
            else:
                cr+=1
                cc-=1
        else:
            if cr==0 or cc==w:
                down = True
                if cc==w:
                    cr+=1
                else:    
                    cc+=1
            else:
                cr-=1
                cc+=1
    return res                
        
def outOfBounds(cc,cr,h,w):
    return cr<0 or cr>h or cc<0 or cc>w

#print(zigzagTraverse([[1,3,4,10],[2,5,9,11],[6,8,12,15],[7,13,14,16]]))
##############################################################
def appartmentSerch(blocks, requirements):
    maxDist = [float("-inf") for block in blocks]
    for i in range(len(blocks)):
        for req in requirements:
            closeDist= float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closeDist = min(closeDist, getDistance(i,j))
            maxDist[i] = max(maxDist[i], closeDist)            
    print(maxDist)        
    return getIndMinVal(maxDist)

def getIndMinVal(array):
    min = 0
    minVal = float("inf")
    for i in range(len(array)):
        cur= array[i]
        if cur<minVal:
            minVal=cur
            min = i
    return min                 

def getDistance(a,b):
    return abs(a-b)

##############################################################

def appartmentSerch2(blocks, requirements):
    minDist = list(map(lambda req: getMinDistances(blocks,req), requirements))
    maxDist = getMaxDistances(blocks, minDist)
    return maxDist

def getMinDistances(blocks, req):
    minDist = [0 for block in blocks]
    closesInd = 888
    for i in range(len(blocks)):
        if blocks[i][req]:  
            closesInd = i
        minDist[i]=getDistance(i, closesInd)    
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closesInd = i
        minDist[i]=getDistance(minDist[i], closesInd)      

    return minDist

def getMaxDistances(blocks, minDist):
    maxDist = [0 for i in blocks]
    for i in range(len(blocks)):
        minDist = list(map(lambda distances: distances[i], minDist))
        maxDist = max(minDist)
    return maxDist    
##############################################################
def apartmentHunting(blocks, reqs):
    contains_utility= []
    for i in range(len(blocks)):
        res = {}
        for k,v in blocks[i].items():
            if k in reqs and v==True: res[k]=i
            #else: res[k]=float("inf")
        contains_utility.append(res)
    contains_utility=findClosestCombination(contains_utility, reqs)
    print(contains_utility)
    return contains_utility.index(min(contains_utility)) 

def findClosestCombination(array, reqs):
    res_dist = []
    for i in range(len(array)):
        for req in reqs:
            if not req in array[i].keys():
                array[i][req] = addReqNext(array, req)                    
    #print(array)
    for i in range(len(array)):
        max_dist =calculateMaxDist(i,list(array[i].values()))
        res_dist.append(max_dist)

    return res_dist

def calculateMaxDist(number,array):
    max = 0
    for i in range(len(array)):
        temp = abs(number-array[i]) 
        if temp > max:
           max=temp
    return max            


##test reverse search algorithm
def addReqNext(array, req):
    res_v_l=float("inf")
    res_v_r=float("inf")
    for i in range(len(array)):
        for k,v in array[i].items():
            if k==req:
                res_v_l = v
    for i in reversed(range(len(array))):
        for k,v in array[i].items():
            if k==req:
                res_v_r = v            
    return min(res_v_l, res_v_r)           

# print(apartmentHunting(blocks = [
#     {
#       "gym": True,
#       "office": False,
#       "pool": False,
#       "school": True,
#       "store": False
#     },
#     {
#       "gym": True,
#       "office": False,
#       "pool": False,
#       "school": False,
#       "store": False
#     },
#     {
#       "gym": False,
#       "office": True,
#       "pool": False,
#       "school": True,
#       "store": False
#     },
#     {
#       "gym": False,
#       "office": True,
#       "pool": False,
#       "school": False,
#       "store": False
#     },
#     {
#       "gym": False,
#       "office": False,
#       "pool": False,
#       "school": False,
#       "store": True
#     },
#     {
#       "gym": True,
#       "office": True,
#       "pool": False,
#       "school": False,
#       "store": False
#     },
#     {
#       "gym": False,
#       "office": False,
#       "pool": True,
#       "school": False,
#       "store": False
#     },
#     {
#       "gym": False,
#       "office": False,
#       "pool": False,
#       "school": False,
#       "store": False
#     },
#     {
#       "gym": False,
#       "office": False,
#       "pool": False,
#       "school": False,
#       "store": False
#     },
#     {
#       "gym": False,
#       "office": False,
#       "pool": False,
#       "school": True,
#       "store": False
#     },
#     {
#       "gym": False,
#       "office": False,
#       "pool": True,
#       "school": False,
#       "store": False
#     }
#   ],
#         reqs = ["gym", "pool", "school", "store"]))