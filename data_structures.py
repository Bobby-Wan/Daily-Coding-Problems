from collections import deque

class SNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class SLinkedList:
    def wipe(self):
        self._headval = None
        self._tailval = None
        self._size = 0
    def __init__(self):
        wipe()

    def get_size(self):
        return self._size

    def add_head(self, value):
        node = SNode(value)
        node.next = self._headval
        self._headval = node
        self._size = self._size + 1

    def add_tail(self, value):
        node = SNode(value)
        if(self._headval == None):
            self._headval = SNode(value)
            self._size += 1
            return
        # while(cur_node.next != None):
        #     cur_node = cur_node.next
        # cur_node.next = node
        # self._size = self._size + 1
        self._tailval.next = node
        self._tailval = node
        self._size += 1


    def add(self, value, index):
        if(index > self._size or index < 0):
            raise Exception('Index out of range..')
        if(index == 0):
            add_head(value)
        elif(index == self._size):
            add_tail(value)
        else:
            node = SNode(value)
            cur_node = self._headval
            for i in range(0, index-1):
                cur_node = cur_node.next
            cur_node.data = value
            self._size += 1
    
    def print(self):
        print('-->', end='')
        if(self._size == 0):
            return
        cur_node = self._headval
        while True:
            print('(',cur_node.data,')-->',end='')
            cur_node = cur_node.next
            if(cur_node == None):
                print()
                return

    def get_value(self, index):
        if(index > self._size-1 or index < 0):
            raise Exception('Index out of range..')
        
        counter = 0
        cur_node = self._headval
        while(counter < index):
            cur_node = cur_node.next
            counter += 1
        return cur_node.data

    def to_list(self):
        values = list()
        current = self._headval
        if not current:
            return []
        
        while current:
            values.append(current.data)
            current = current.next
        
        return values
    
    def fill_from_list(self, lst):
        wipe()
        if lst:
            for value in lst:
                self.add_tail(value)
        
class BT_Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'<{self.data}, {self.left}, {self.right}>'


def build_binary_tree(values, index):
    if len(values) == 0:
        raise Exception('Node list is empty')

    if index > len(values) - 1:
        raise Exception('Index out of range')

    root = BT_Node(values[index])
    if 2*index+1 < len(values) and values[2*index+1] is not None:
        root.left = build_binary_tree(values, 2*index+1)
    if 2*index+2 < len(values) and values[2*index+2] is not None:
        root.right = build_binary_tree(values, 2*index+2)

    return root

def max_bst_node(root):
    if root is None:
        return None
    print('current: ' + str(root.data))
    if root.right and root.right.data:
        max = max_bst_node(root.right)
    else:
        max = root.data

    return max
