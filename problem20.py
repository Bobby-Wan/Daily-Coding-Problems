# This problem was asked by Google.
# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.


#O(N) space complexity
#O(M+N) time complexity
import basics
from data_structures import SLinkedList

def commonNode(list1, list2):
    number_set = set()
    for i in range(list1.get_size()):
        number_set.add(list1.get_value(i))
    
    for i in range(list2.get_size()):
        if(list2.get_value(i) in number_set):
            return list2.get_value(i)

def main():
    l1 = basics.getNumberList()
    l2 = basics.getNumberList()
    list1 = SLinkedList()
    list2 = SLinkedList()

    for i in range(0,len(l1)):
        list1.add_tail(l1[i])
    for i in range(0,len(l2)):
        list2.add_tail(l2[i])

    common_element = commonNode(list1,list2)
    print('First common element: ', common_element)
    
if __name__ == '__main__':
    main()