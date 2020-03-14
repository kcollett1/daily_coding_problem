#########################################################################
#      Daily Coding Problem #43                                         #
#                                                                       #
# Implement a stack that has the following methods:                     #
#                                                                       #
#    push(val): which pushes an element onto the stack                  #
#                                                                       #
#    pop():     which pops off and returns the topmost element          #
#               of the stack. If there are no elements in the           #
#               stack, then it should throw an error or return null.    #
#                                                                       #
#    max():     which returns the maximum value in the stack            #
#               currently. If there are no elements in the stack,       #
#               then it should throw an error or return null.           #
#########################################################################

class stack_node: # singly linked list with max_val to track max in stack
    def __init__(self, val=None, max_val=None, nex=None):
        '''instantiate a node object for part of stack object'''
        self.val = val
        self.nex = nex
        self.max_val = max_val

class stack:
    def __init__(self, init_val=None):
        '''instantiate stack with initial val if provided
           or empty if no value is passed'''
        if not init_val:
            self.head = None
        else:
            self.head = stack_node(init_val, init_val)

    def push(self, val):
        '''O(1) time. set up new node to add to stack
           and change current head pointer'''
        max_val = val
        if self.head and self.head.max_val > max_val:
            max_val = self.head.max_val
        self.head = stack_node(val, max_val, self.head)

    def pop(self):
        '''O(1) time. retrieve current top val,
           and change current head pointer'''
        if not self.head: # empty stack, can't pop anything off
            return None
        top_val = self.head.val
        self.head = self.head.nex
        return top_val

    def peek(self):
        ''' aka top, O(1) time. return top val if
            it exists without altering the stack'''
        if not self.head: return None
        return self.head.val

    def max(self):
        '''O(1) time. retrieve head nodes max_val
           attribute if it exists'''
        if not self.head: return None
        return self.head.max_val

newStack = stack()
print('should be None, empty stack so far:', newStack.pop())
newStack.push(4)
newStack.push(5)
newStack.push(3)
newStack.push(7)
newStack.push(4)
newStack.push(4)
print('should be 4 and 7:', newStack.peek(), newStack.max())
newStack.pop() # remove 4, max still 7
newStack.pop() # remove 4, max still 7
newStack.pop() # remove 7, max 5, peek 3
print('should be 3 and 5:', newStack.peek(), newStack.max())

newStack = stack(5)
print('5:', newStack.peek())
newStack.push(145)
print('145:', newStack.max())
newStack.push(-1)
print('145:', newStack.max())
newStack.pop()
print('145:', newStack.max())
newStack.pop()
print('5:', newStack.max())
newStack.pop()
print('None:', newStack.max())
newStack.pop()
print('None:', newStack.max())
newStack.push(-10)
print('-10:', newStack.max())
