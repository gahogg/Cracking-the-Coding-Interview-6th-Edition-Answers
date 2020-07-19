# Implement an algorithm to delete a node in the middle
# (i.e any node but the first and last node, not necessarily
# the exact middle) of a singly linked list, given only access to that node.
from singly_linked_list_node import SinglyLinkedListNode


# O(n) runtime, O(1) space
def del_middle_node(node):
    prev = node
    cur = node
    do = False
    while cur.next:
        if do:
            prev = prev.next
        else:
            do = True
        cur.data = cur.next.data
        cur = cur.next
    prev.next = None


head = SinglyLinkedListNode.linkify([3, 1, 2, 5, 1, 4, 1])
print(head)
second_node = head.ith_node(1)
del_middle_node(second_node)
print(head)