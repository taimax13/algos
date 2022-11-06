#annograms through hash table
from contextlib import nullcontext


def are_anagrams(s1,s2):
  if len(s1) != len(s2):
    return False
  freq1 = get_hash_from_s(s1, {})
  freq2 = get_hash_from_s(s2, {})
  count=0
  for k in freq1:
    if k in freq2 and freq2[k] == freq1[k]:
      count+=1
    else:
      return False
  return True    

def get_hash_from_s(s, freq1):
  for ch in s:
    if ch in freq1:
      freq1[ch]+=1
    else:
      freq1[ch] =1      
  return freq1

#print(are_anagrams("ankka","auuna"))


def twoNumberSum(array, targetSum):
    dict_items= {}
    result = []
    for item in array:
        dict_items[item]=targetSum-item
    print(dict_items)
    for k,v in dict_items.items():
      if v!=k and v in dict_items.keys():
        return([k,v])
    return []
#print(twoNumberSum([3,5,-4,8,11,1,-1,6], 10))    


############################################
def isValidSubsequence(array, sequence):
    arrInd=0
    seqInd=0
    while arrInd < len(array) and seqInd < len(sequence):
        if array[arrInd] == sequence[seqInd]:
            seqInd +=1
        arrInd+=1
    return seqInd==len(sequence)
#print(isValidSubsequence([4,5,6,7], [6,7]))
################################################################
## sorted squered array 
def sortedSqueredArray(arr):
  dict_sorted = {}
  arr_res=[]
  i=0
  while i < len(arr):
    squreNum = arr[i]**2
    if squreNum in dict_sorted.keys():
      dict_sorted[squreNum]+=1
    else: dict_sorted[squreNum]=1
    i+=1 
  #print(dict_sorted)
  for k, v in dict_sorted.items():
    #print(k,v)
    while v > 0:
      arr_res.append(k)
      v-=1  
  return sorted(arr_res) 
#print(sortedSqueredArray([4,8,8,8,6,7]))

################################
def tournamentWinner(competitions, results):
    res = {}
    for i, competition in enumerate(competitions):
        homeTeam,awayTeam = competition
        if results[i]==0:
            value=res.setdefault(awayTeam,0)
            res[awayTeam]=value+1
        else:
            value=res.setdefault(homeTeam,0)
            res[homeTeam] = value+1
    #return max(res, key=res.get)

#print(tournamentWinner([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"],],[0,0,1]))    


################################

def binarySearch(v, To_Find):
    lo = 0
    hi = len(v) - 1
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if v[mid] < To_Find:
            lo = mid + 1
        else:
            hi = mid
 
    if v[lo] == To_Find:
        return lo
    elif v[hi] == To_Find:
        return hi
    else:
        return -1
#print(binarySearch([5,6,7,8,9], 8))
# 
# 
#######################################
def productSum(array):
  res=0
  count = 1
  for item in array:
    res=countSum(item,count,res)
  return res  

def countSum(item,count,res):
  if type(item)!=list:
    res+=(item*getFactorial(count))
  else:
    count+=1
    for arr in item:
      res=countSum(arr,count,res)
  return res  

def getFactorial(count):
  fact=1
  print(count)
  for i in range(1,count+1):
    fact = fact*i
  return fact  

#print(getFactorial(5))
    
# print(productSum([
#     [
#       [
#         [
#           [5]
#         ]
#       ]
#     ]
#   ]))


################################
def getNthFib(n):
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return getNthFib(n-1) + getNthFib(n-2)
#print(getNthFib(5))    

################################
def getFactorial2(n):
  fact=0
  res=[0,1]
  if n==0 or n==1:
    return 0   
  for i in range(2,n):
    task = res[i-2]+res[i-1]
    res.append(task)
  return res[len(res)-1]

#print(getFactorial2(1))
######################################################################

def bubbleSort(array):
  for i in range(len(array)):
    swapped = False
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        swapped = True
    if not swapped:
      break
  return array    
#print(bubbleSort([456,8,90,1,2,3]))

###############################################################################
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 
    lst = [] #empty list to store sorted elements
    print("Sorted array is : ")
    for i in range(len(arr)):
        lst.append(arr[i])
    return lst         #appending the elements in sorted order

#print(insertionSort([1,2,3]))
 

   

# def reverse_list(head: ListNode) -> NodeList:
#     if not head:
#         return None
#     newHead = head
#     if head.next:
#         newHead = reverse_list(head.next)
#         head.next.next = head
#     head.next = None
#     return newHead        

# print(reverse_list([1,2]))        
