# This problem was asked by Google.

# An XOR linked list is a more memory 
# efficient doubly linked list. 
# Instead of each node holding next and prev fields, 
# it holds a field named both, which is an XOR 
# of the next node and the previous node. 
# Implement an XOR linked list; 
# it has an add(element) which adds the element to 
# the end, and a get(index) which returns the node 
# at index.

# If using a language that has no pointers 
# (such as Python), you can assume you have access 
# to get_pointer and dereference_pointer functions 
# that converts between nodes and memory addresses.

def get_by_address(address, global_vars):
    if address == 0:
        return None

    return [x for x in global_vars.values() if id(x) == address][0]

class Node:
    def __init__(self, val, both):
        self.val = val
        self.both = both


class XORLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def print_(self):
        if self.first is None:
            print('none')
        else:
            current = self.first
            print(current.val)
            last = None
            next =  0 ^ current.both
            while current != get_by_address(id(self), locals()).last:
                last = id(current)
                current = get_by_address(next, globals())
                print(current.val)
                next = last ^ current.both

    def add(self, node):
        if self.first is None and self.last is None:
            self.first = get_by_address(id(node), globals())
            self.last = get_by_address(id(node), globals())
        else:
            if self.first == self.last:
                self.first.both = 0^ id(node)
                self.last.both = 0^id(node)
                node.both = id(self.last)^ 0
                self.last = node
            else:
                current = self.first
                last = 0
                next = current.both ^ last
                while next != id(self.last):
                    last = id(current)
                    current = get_by_address(next, globals())
                    next = current.both ^ last
                self.last.both = id(current) ^ id(node)
                node.both = id(self.last) ^ 0
                self.last = get_by_address(id(node), globals())
             
    def get(self, index):
        if self.first is None:
            raise Exception('Out of bound')

        temp = self.first
        next = 0 ^ temp.both
        while index > 0:
            if next == 0:
                raise Exception('Out of bound')
            
            last = temp
            temp = get_by_address(next, globals())
            next = id(last) ^ temp.both
            index = index - 1
            
        return temp

first_node = Node('first', 0)
second_node = Node('second', 0)
third_node = Node('third', 0)
fourth_node = Node('fourth', 0)
fifth_node = Node('fifth',0)


def main():
    xor_list = XORLinkedList()
    
    xor_list.add(first_node)
    xor_list.add(second_node)
    xor_list.add(third_node)
    xor_list.add(fourth_node)
    xor_list.add(fifth_node)
    xor_list.print_()
    
if __name__ == '__main__':
    main()