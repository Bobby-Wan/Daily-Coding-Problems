# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# Given a singly linked list and an integer k, remove the kth last element from 
# the list. k is guaranteed to be smaller than the length of the list.
# The list is very long, so making more than one pass is prohibitively expensive.
# Do this in constant space and in one pass.

from data_structures import SNode as Node

def remove_kth_last(head, k):
    if not head or not k:
        return head
    
    dummy = Node(None)
    dummy.next = head
    current_node = dummy
    runner = head

    for _ in range(k):
        runner = runner.next
    while runner:
        current_node = current_node.next
        runner = runner.next
    
    current_node.next = current_node.next.next

    return dummy.next

def to_list(head):
    if not head:
        return []

    values = list()
    current = head
    while(current):
        values.append(current.data)
        current = current.next
    return values

def to_linked_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for i in range(len(lst)-1):
        current.next = Node(lst[i+1])
        current = current.next
    
    return head
        

def main():
    head = to_linked_list([1,2,3])

    
    print(to_list(remove_kth_last(head,2)))
if __name__ == '__main__':
    main()