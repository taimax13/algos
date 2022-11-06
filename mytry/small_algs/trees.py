

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