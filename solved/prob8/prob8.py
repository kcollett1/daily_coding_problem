class Node:
    def __init__(self, val, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# this is brute force O(n^2) I think, not sure if this can be done better
def everything_below_same(root):
    if not root: return False
    if not root.left and not root.right: return True

    val_left  = True
    left_down = True
    if root.left:
        val_left = (root.val == root.left.val)
        left_down = everything_below_same(root.left)

    val_right  = True
    right_down = True
    if root.right:
        val_right = (root.val == root.right.val)
        right_down = everything_below_same(root.right)

    return val_left and left_down and val_right and right_down

def num_unival_subtrees(root):
    if not root: return 0
    thisnode = 0
    if everything_below_same(root): thisnode = 1
    return thisnode + num_unival_subtrees(root.left) + num_unival_subtrees(root.right)

test_tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print('ans should be False:', everything_below_same(test_tree))
print('ans should be True:', everything_below_same(test_tree.left))
print('ans should be True:', everything_below_same(test_tree.right.left))
print('ans should be 5:', num_unival_subtrees(test_tree))

test_tree = Node(0, Node(0), Node(0, Node(0, Node(0), Node(0)), Node(0)))
print('ans should be 7:', num_unival_subtrees(test_tree))

test_tree = Node(0, Node(1), Node(0, Node(0, Node(1), Node(1)), Node(0)))
print('ans should be 4:', num_unival_subtrees(test_tree))

test_tree = Node(0, Node(0, Node(0), Node(0)), Node(0, Node(0, Node(0), Node(0)), Node(0)))
print('ans should be 9:', num_unival_subtrees(test_tree))

test_tree = Node(0, Node(1), Node(2, Node(3, Node(4), Node(5)), Node(6)))
print('ans should be 4:', num_unival_subtrees(test_tree))
