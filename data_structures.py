class SNode:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
    
class SLinkedList:
    def __init__(self):
        self._headval = None
        self._tailval = None
        self._size = 0

    def get_size(self):
        return self._size

    def add_head(self, value):
        node = SNode(value)
        node.nextval = self._headval
        self._headval = node
        self._size = self._size + 1

    def add_tail(self, value):
        node = SNode(value)
        if(self._headval == None):
            self._headval = SNode(value)
            self._size += 1
            return
        cur_node = self._headval
        # print('Tail Node value: ',cur_node.dataval)
        while(cur_node.nextval != None):
            cur_node = cur_node.nextval
            # print(cur_node.dataval)
        cur_node.nextval = node
        self._size = self._size + 1

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
                cur_node = cur_node.nextval
            cur_node.dataval = value
            self._size += 1
    
    def print(self):
        print('-->', end='')
        if(self._size == 0):
            return
        cur_node = self._headval
        while True:
            print('(',cur_node.dataval,')-->',end='')
            cur_node = cur_node.nextval
            if(cur_node == None):
                print()
                return

    def get_value(self, index):
        if(index > self._size-1 or index < 0):
            raise Exception('Index out of range..')
        
        counter = 0
        cur_node = self._headval
        while(counter < index):
            cur_node = cur_node.nextval
            counter += 1
        return cur_node.dataval

    def to_list(self):
        values = list()
        current = self._headval
        if not current:
            return []
        
        while current:
            values.append(current.nextval):
        
        return values

class BT_Node:
    def __init__():
        self.data = data
        self.left = left
        self.right = right 