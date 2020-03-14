class Node:
# assuming in this problem that val is a str
    def __init__(self, val, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

def serialize(root):
    if not root or not root.val: return "Node(None)"
    return "Node('" + root.val + "', " + serialize(root.left) + ", " + serialize(root.right) + ")"

def deserialize(s):
    return eval(s)

#### test cases:
testnode   = Node('root', Node('left', Node('left.left')), Node('right'))
ser_test   = serialize(testnode)
deser_test = deserialize(serialize(testnode))
ser_deser_ser = serialize(deser_test)
print('serialized:', ser_test)
print('deserialized:', ser_deser_ser)
print('serialize == serialize(deserialize(serialize())?', ser_test == ser_deser_ser)
print('left.left?:', deser_test.left.left.val)
print('left?:', deser_test.left.val)
print('right?:', deser_test.right.val)
print('')

testnode   = Node('root', Node('left', Node('leftleft', Node('leftleftleft', Node('leftleftleftleft', Node('leftleftleftleftleft', Node('leftleftleftleftleftleft')),Node(''))))), Node('right', Node('rightleft'), Node('rightright')))
ser_test   = serialize(testnode)
deser_test = deserialize(serialize(testnode))
ser_deser_ser = serialize(deser_test)
print('serialized:', ser_test)
print('after being deserialized:', serialize(deser_test))
print('serialize == serialize(deserialize(serialize())?', ser_test == ser_deser_ser)
