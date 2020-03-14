# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).
# ex: "([])[]({})" : True
# ex: "([)]" : False
# ex: "((()" : False

class node: # singly linked list
    def __init__(self, val=None, nextnode=None):
        self.val = val
        self.next = nextnode

class queue: # methods add and remove (pop) adds new val to beginning and removes/returns most recently added val
    def __init__(self, head=None):
        self.head = head

    def add(self, val): # add val to beginning of queue, new head pointer points to prev head pointer
                        # if currently empty, new head pointer will just point to None
        self.head = node(val, self.head)

    def remove(self): # remove most recently added val, return val
        if not self.head:
            return 0 # empty queue

        val = self.head.val
        self.head = self.head.next

        return val


def well_formed(s): # s = string made up of only round, curly, square open/close brackets
    q = queue()
    match = {')':'(', '}':'{', ']':'['}

    for bracket in s:
        if bracket in ('[','{','('): # add opening bracket to queue
            q.add(bracket)
        else: # make sure closing bracket matches prev opening bracket (if it exists), if so remove it from queue
            if q.remove() != match[bracket]:
                return False

    # check if any opening brackets remain unmatched
    # None means empty queue which means all brackets were properly matched, if any remain it is an unmatched expression
    return not q.head

test_str = '([])[]({})'
print('should be True:', well_formed(test_str))
test_str = '([)]'
print('should be False:', well_formed(test_str))
test_str = '((()'
print('should be False:', well_formed(test_str))
