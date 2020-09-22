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

def serialize(root):
    StaticHolder.index = 0
    return to_string(root)

def to_string(root):
    if root == None:
        result = 'none '
    else:
        result = root.val + ' ' + to_string(root.left) + to_string(root.right)
    return result

def deserialize(string):
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
        left = deserialize(' '.join(values))
        right = deserialize(' '.join(values))
        node = Node(root, left, right)

    return node

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    assert deserialize(serialize(node)).right.val == 'right'

    print(serialize(node))


if __name__ == '__main__':
    main()