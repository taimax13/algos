# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
from queue import Queue


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children: 
            child.depthFirstSearch(array)
        return array    

##############################################################

def hasSingleCycle(array):
    visit = 0
    cur_index = 0
    while visit < len(array):
        if visit > 0 and cur_index == 0:
            return False
        visit += 1    
        cur_index = getNextInd(cur_index, array)
    return cur_index == 0    


def getNextInd(ind, array):
    jump = array[ind]
    next_i = (ind + jump) % len(array)
    return next_i if next_i >= 0 else next_i + len(array)

##############################################################
# grapth-traverse
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        q= [self]
        while len(q) > 0:
            current = q.pop(0)
            array.append(current.name)
            for child in current.children:
                q.append(child)
        return array





        


    
