# remove k-th last element from the list in constant space and in one pass through the list
# k guaranteed to be less than length of list, implemented without this constraint anyway

class singlylinkednode:
    def __init__(self, val = None, nextptr = None):
        self.val = val
        self.next = nextptr

def remove_kthlast(l, k):
    if k <= 0:
        return l

    ahead,behind = l,l
    for _ in range(k):
        if not ahead:
            # k is larger than length of list, so return list unchanged
            return l
        ahead = ahead.next

    # go to last element in linked list with ahead pointing k elements ahead of behind pointer
    while ahead.next:
        ahead, behind = ahead.next, behind.next

    # remove node that behind points to
    behind.next = behind.next.next

    # return altered linked list with kth last element removed
    return l

k = 57
linkedlist_test = None
for i in range(1, 101):
    newnode = singlylinkednode(i, linkedlist_test)
    linkedlist_test = newnode

# test - should remove node with val = k (just because of the way linkedlist_test was defined)
remove_kthlast(linkedlist_test, k)
node = linkedlist_test
print('node with val', k, 'should be gone...')
while node:
    print('   ', node.val)
    node = node.next
# tested with k=0,1,3,57,99,100,101
