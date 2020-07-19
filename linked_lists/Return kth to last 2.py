# Implement an algorithm to find the kth to last element
# of a singly linked list
from singly_linked_list_node import SinglyLinkedListNode


# O(n) runtime, O(1) space
def kth_to_last(head, k):
    cur = head
    while True:
        k -= 1
        if k == 0:
            return cur
        cur = cur.next


head = SinglyLinkedListNode.linkify([3, 3, 2, 2, 1, 4, 1])
print(head)
print(kth_to_last(head, 8))