class node:
    '''node for linked list type structures'''
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __repr__(self):
        return str(self.val)

class stack:
    '''stack data structure (Last in First out)'''
    def __init__(self):
        self.top = None
        self.size = 0

    def add(self, val):
        newNode = node(val)
        newNode.next = self.top
        self.top = newNode
        self.size += 1

    
    def get(self):
        if self.top == None:
            return None
        else:
            topVal = self.top
            self.top = topVal.next
            self.size -= 1
            return topVal.val

    