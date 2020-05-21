# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class StaticHolder:
    index = 0
    
def is_leaf(node):
    if node.left == None and node.right == None:
        return True
    return False

def is_unival(node, value):
    if is_leaf(node):
        return True
    if ((node.val == node.left.val) and (node.right == None) and is_unival(node.left, node.val)) or \
    ((node.val == node.right.val) and (node.left == None) and is_unival(node.right, node.val)) or \
    ((node.val == node.left.val) and (node.val == node.right.val)):
        return True
    return False

def get_unival_count(root):
    if root == None:
        return 0
    if is_unival(root, root.val):
        return 1 + get_unival_count(root.left) + get_unival_count(root.right)
    return  get_unival_count(root.left) + get_unival_count(root.right)

def main():
    root = Node(0, Node(1),Node(0,Node(1,Node(1),Node(1)),Node(0)))
    print get_unival_count(root)
    
if __name__ == '__main__':
    main()