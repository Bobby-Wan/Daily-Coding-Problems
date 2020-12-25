# This problem was asked by Dropbox.
# Given the root to a binary search tree, 
# find the second largest node in the tree.

from data_structures import BT_Node, build_binary_tree, max_bst_node

def second_largest(root):
    if not root:
        raise Exception('Invalid root node')

    if not root.right:
        return max_bst_node(root.left)
    
    if root.right.right:
        # print('switching to ' + str(root.right.data))
        return second_largest(root.right)
    
    if root.right.left:
        # print('comparing ' + root.data + max_bst_node(root.right.left))
        return max(root.data, max_bst_node(root.right.left))
    else:
        return root.data
        
if __name__ == "__main__":
    node_values = [8,3,10,1,6,None,14,None,None,4,7,None,None,13]
    root = build_binary_tree(node_values, 0)
    print(root)
    print(second_largest(root))

