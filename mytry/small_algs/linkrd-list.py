class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList
    while current is not None:
        next = current.next
        while next is not None and next.value == current.value:
            next = next.next

        current.next = next    
        current = next

    return linkedList    
