def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        tmpnext = curr.next
        curr.next = prev
        prev = curr
        curr = tmpnext
        # equivalent:
        #prev, curr.next, curr = curr, prev, curr.next
    head = prev
    return head

def find_intersection(A, B):
    A = reverse_linked_list(A) # O(A)
    B = reverse_linked_list(B) # O(B)

    A_itr = A # const space, just one node
    B_itr = B # const space, just one node

    while A_itr.next and B_itr.next and A_itr.next.value == B_itr.next.value: # at most, O(max(A,B))
        A_itr = A_itr.next
        B_itr = B_itr.next

    # answer found, node is A_itr and B_itr
    print('answer, intersecting node has value of:', A_itr.value)

    # restore order of original linked lists, again just O(max(A,B))
    A = reverse_linked_list(A)
    B = reverse_linked_list(B)

    return 1 # success

# make tests to test this out...
