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

    result =  [x for x in global_vars.values() if id(x) == address]
    if(len(result)):
        return result[0]
    else:
        return None

class Node:
    def __init__(self, val, both):
        self.val = val
        self.both = both

class XORLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def print_(self):
        if not self.first:
            return
        else:
            current = self.first
            prev = None
            next =  0 ^ current.both
            print(current.val)
            while current is not self.last:
                prev = id(current)
                current = get_by_address(next, globals())
                print(current.val)
                next = prev ^ current.both

    def empty(self):
        return self.first is None and self.last is None

    def add(self, node):
        if self.empty():
            node.both = 0
            self.first = node
            self.last = node
        else:
            self.last.both = self.last.both ^ id(node)
            node.both = id(self.last)
            self.last = node

            # #if list has one element
            # if self.first is self.last:
            #     self.first.both = 0 ^ id(node)
            #     node.both = id(self.first) ^ 0
            #     self.last = node
            # else:
            #     current = self.first
            #     prev = 0
            #     next = current.both ^ prev
            #     while next != id(self.last):
            #         prev = id(current)
            #         current = get_by_address(next, globals())
            #         if not current:
            #             current = get_by_address(next, locals())
            #         next = current.both ^ prev
            #     self.last.both = id(current) ^ id(node)
            #     node.both = id(self.last) ^ 0
            #     self.last = get_by_address(id(node), globals())
        
    def get(self, index):
        if self.first is None:
            raise Exception('Out of bound')

        current = self.first
        last = 0
        next = last ^ current.both
        for _ in range(index):
            if next == 0:
                raise Exception('Out of bound')
            last = current
            current = get_by_address(next, globals())
            next = id(last) ^ current.both
            
        return current



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

    print(xor_list.get(3).val)    
if __name__ == '__main__':
    main()