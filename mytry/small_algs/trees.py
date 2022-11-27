

###########################################################################


# simple binary tree
# in this implementation, a node is inserted between an existing node and the root

class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())
            


# test tree

def testTree():
    myTree = BinaryTree("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    printTree(myTree)

#print(testTree())

#################################################################################        
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current=self
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BST(value)
                    break
                else:
                    current = current.left
            else:
                if current.right in None:
                    current.right = BST(value)
                    break
                else:    
                    current = current.right        
        return self

    def contains(self, value):
        current = self
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right    
            else:
                return True
        return False        

    def remove(self, value, parent=None):
        current = self
        while current is not None:
            if value < current.value:
                parent = current
                current = current.left
            elif value> current.value:
                parent = current
                current = current.right
            else:
                if current.left is not None and current.right is not None:
                    current.value = current.right.getMin() 
                    current.right.remove(current.value, current)
                elif parent == None:
                    if current.left is not None:
                        current.value =current.left.value
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.right is not None:
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    else:
                        current.value = None    
                elif parent.left == current:
                    parent.left = current.left if current.left is not None else current.right
                elif parent.right == current:
                    parent.right = current.left if current.left is not None else current.right  
                break      
        return self

    def getMin(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value   

###################################################################################
##recursively

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, closest=float("inf"))


def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest)> abs(target - tree.value):
        closest =tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest            


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

###########################################################################
## iteratively
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, closest=float("inf"))


def findClosestValueInBstHelper(tree, target, closest):
    current = tree
    while current is not None:
        if tree is None:
            return closest
        if abs(target - closest)> abs(target - current.value):
            closest =current.value
        if target < current.value:
            current = current.left
        elif target > tree.value:
            current = current.right
        else:
            break
    return closest            


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

###################################################################
## This is an input class. Do not edit.

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, min, max):
    if tree is None:
            return True
    if tree.value and tree.value < min or tree.value >= max:
        return False
    leftValid = validateBstHelper(tree.left, min, tree.value)
    return leftValid and validateBstHelper(tree.right, tree.value, max)


###################################################################

def inOrderTraverse(tree, array):
    if tree is None:
        return array
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
    return array    

def preOrderTraverse(tree, array):
    if tree is None:
        return array
    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
    return array     


def postOrderTraverse(tree, array):
    if tree is None:
        return array
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array


 ##############################################################   
def minHeightBst(array):
    return minHeightBstHelper(array, None,0,len(array)-1)

def minHeightBstHelper(array, bst, start, end):
    if start > end:
        return
    mid = (start+end)//2
    addVal = array[mid]
    if bst is None:
        bst=BST(addVal)
    else:        
        bst.insert(addVal)
    minHeightBstHelper(array, bst, start, mid - 1)
    minHeightBstHelper(array, bst, mid +1, end)

    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

def minHeightBst(array):
    return minHeightBstHelper(array, None,0,len(array)-1)

def minHeightBstHelper(array, bst, start, end):
    if start > end:
        return
    mid = (start+end)//2
    addVal = array[mid]
    if bst is None:
        bst=BST(addVal)
    else:        
        bst.insert(addVal)
    minHeightBstHelper(array, bst, start, mid - 1)
    minHeightBstHelper(array, bst, mid +1, end)

    return bst

###################################################################
def minHeightBst(array):
    return minHeightBstHelper(array, None,0,len(array)-1)

def minHeightBstHelper(array, bst, start, end):
    if start > end:
        return
    mid = (start+end)//2
    newNode = BST(array[mid])
    if bst is None:
        bst = newNode
    else:
        if array[mid] < bst.value:
            bst.left = newNode
            bst = bst.left  
        else :
            bst.right = newNode
            bst = bst.right     
    minHeightBstHelper(array, bst, start, mid - 1)
    minHeightBstHelper(array, bst, mid +1, end)

    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

########################################################################
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums=[]
    calculateBranchSums(root,0,sums)
    return sums


def calculateBranchSums(node,sum, sums):
    if node is None:
        return 
    newSum = sum +node.value
    if node.left is None and node.right is None:
        sums.append(newSum)
        return

    calculateBranchSums(node.left, newSum,sums)
    calculateBranchSums(node.right,newSum, sums)    


######################stack solution########################################
def nodeDepths(root):
    sum=0
    stack = [{"node":root, "depth":0}]
    while len(stack)>0:
        nodeUnit = stack.pop()
        node, depth = nodeUnit("node"), nodeUnit("depth")
        if node is None:
            continue
        sum+=depth
        stack.append({"node":node.left, "depth":depth + 1})
        stack.append({"node":node.right, "depth": depth + 1})
    return sum    
###recursively
def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth+nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth +1)    



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


###################################################################
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, visited, value):
        self.visited = visited
        self.value = value

def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    revInOrder(tree,k, treeInfo)
    return treeInfo.value

def revInOrder(node,k, treeInfo):
    if node == None or treeInfo.value >k:
        return
    revInOrder(node.right,k,treeInfo) 
    if treeInfo.visited < k:
        treeInfo.visited +=1
        treeInfo.value = node.value
        revInOrder(node.left,k, treeInfo)


 ########################################################################
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    sortedVal=[]
    inOrderTraverse(tree, sortedVal)
    return sortedVal[len(sortedVal)-k]


def inOrderTraverse(node, sortedVal):
    if node ==None:
        return
    inOrderTraverse(node.left, sortedVal)
    sortedVal.append(node.value)
    inOrderTraverse(node.right, sortedVal)



######min hip
# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        parentInd = (len(array)-2) // 2
        for i in reversed(range(parentInd)):
            self.siftDown(i,len(array)-1, array)
        return array
    def siftDown(self, currentInd, endInd, heap):
        child1ind = currentInd *2 +1
        while child1ind <=endInd:
            child2ind = currentInd*2+2 if currentInd*2+2 <=endInd else -1
            if child2ind != -1 and heap[child2ind]<heap[child1ind]:
                indSwap = child1ind
            else:
                indSwap = child2ind
            if heap[indSwap]<heap[currentInd]:
                self.swap(currentInd, indSwap, heap)
                currentInd = indSwap
                child1ind= currentInd *2+1
            else:
                break


    def siftUp(self, currentInd, heap):
        parentInd = (currentInd-1)//2
        while currentInd>0 and heap[currentInd]<heap[parentInd]:
            self.swap(currentInd, parentInd, heap)
            currentInd=parentInd
            parentInd = (currentInd-1)//2


    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        removed = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return removed
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)
    def swap(self, i,j,heap):
        heap[i], heap[j] = heap[j], heap[i]