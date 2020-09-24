# Given the root to a binary tree, implement serialize(root), which serializes the tree
# into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class StaticHolder:
    index = 0

def deserialize(root):
    StaticHolder.index = 0
    return to_node(root)

def serialize(root):
    if root == None:
        result = 'none '
    else:
        result = root.val + ' ' + serialize(root.left) + serialize(root.right)
    return result

def to_node(string):
    if string == None:
        return None
    values = string.split()
    if values == []:
        return None
    
    if len(values) <= (StaticHolder.index - 1):
        return None
    if values[StaticHolder.index] == 'none':
        StaticHolder.index += 1
        return None
    else:
        root = values[StaticHolder.index]
        StaticHolder.index += 1
        left = to_node(' '.join(values))
        right = to_node(' '.join(values))
        node = Node(root, left, right)

    return node

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    assert deserialize(serialize(node)).right.val == 'right'

    print(serialize(node))

if __name__ == '__main__':
    main()