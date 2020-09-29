# Daily Coding Problem: Problem #24
# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# Implement locking in a binary tree. A binary tree node can be locked or 
# unlocked only if all of its descendants or ancestors are not locked.
# Design a binary tree node class with the following methods:
# -is_locked, which returns whether the node is locked
# -lock, which attempts to lock the node. If it cannot be locked, 
# then it should return false. Otherwise, it should lock it and return true.
# -unlock, which unlocks the node. If it cannot be unlocked, then it should return false. 
# Otherwise, it should unlock it and return true.
# You may augment the node to add parent pointers or any other property you would like. 
# You may assume the class is used in a single-threaded program, so there is no need for 
# actual locks or mutexes. Each method should run in O(h), 
# where h is the height of the tree.

# Даниъл Шпатов
# Даниел Писарски

class Lockable_BT_Node:
    def __init__(self, data, locked, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.locked = locked
        self.has_locked_children = False

    #O(1) time complexity, n = number of nodes in tree
    def are_children_unlocked(self):
        return not(self.has_locked_children)

    #O(h) time complexity, h = height of tree
    def are_parents_unlocked(self):
        if(self.parent):
            if(self.parent.locked):
                return False
            if(not(self.parent.are_parents_unlocked())):
                return False

            return True

    #O(n) = O(n) time complexity, n = number of nodes in tree
    def is_state_changeable(self):
        if(self.are_parents_unlocked() or self.are_children_unlocked()):
            return True
        return False

    #O(h) time complexity, h = height of tree
    def insert(self,value, lock_state):
        if(lock_state):
            self.has_locked_children = True

        if(self.data >= value):
            if(self.left):
                self.left.insert(value, lock_state)
                return
            else:
                self.left = Lockable_BT_Node(value, lock_state, self)
                return
        if(self.data < value):
            if(self.right):
                self.right.insert(value, lock_state)
                return
            else:
                self.right = Lockable_BT_Node(value, lock_state, self)
                return
    
    def is_locked(self, node):
        return node.locked

    #O(n) time complexity, n = number of nodes in tree
    def lock(self):
        if(self.is_state_changeable()):
            self.locked = True
            return True
        return False

    #O(n) time complexity, n = number of nodes in tree
    def unlock(self):
        if(self.is_state_changeable()):
            self.locked = False
            return True
        return False
    
def main():
    root = Lockable_BT_Node(1, True)
    root.insert(-1,False)
    root.insert(0,False)
    root.insert(3,False)
    root.insert(2, False)

    assert root.data == 1
    assert root.left.data

    print('Left: ', root.left.data)
    print('Left right: ', root.left.right.data)
    print('Right: ', root.right.data)
    print('Right left: ', root.right.left.data)
    
    print('Right state: ', root.right.locked)
    
    print('Right lock succeeded', root.right.lock())
    print('Right locked: ', root.right.locked)
    print('Root has locked children: ', root.has_locked_children)
    print('Left has locked children: ', root.left.has_locked_children)
    print('Root before locking: ', root.locked)
    print('Unlocking root: ', root.unlock())    
    print('Root after locking: ', root.locked)

    


if __name__ == '__main__':
    main()