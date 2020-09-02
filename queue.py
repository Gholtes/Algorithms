class node:
    '''node for linked list type structures'''
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return str(self.val)

class queue:
    '''queue data structure (First in First out)'''
    def __init__(self):
        self.last = None
        self.first = None
        self.size = 0
    
    def add(self, val):
        newNode = node(val)
        #if the queue is empty, set the new node as a the first item
        if self.first == None:
            self.first = newNode
        #the next node after the new node is always the current last node, even if the list is empty and the last item is none
        newNode.next = self.last

        #if there is no last node (empty queue), skip this. 
        #Otherwise set the current last node's previous value to the new node.
        if self.last != None:
            self.last.prev = newNode
        #the last item in the queue is always the new node
        self.last = newNode
        self.size += 1

    def get(self):
        #skip if the queue is empty
        if self.first == None:
            return None
        else:
            #return the first item in the queue, reset the first item to the next
            nextNode = self.first
            self.first = nextNode.prev
            self.size -= 1
            return nextNode.val

