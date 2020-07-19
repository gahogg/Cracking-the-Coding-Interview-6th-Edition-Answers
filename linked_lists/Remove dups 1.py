# Write code to remove duplicates from an unsorted linked list
from singly_linked_list_node import SinglyLinkedListNode


# O(n) runtime, O(n) space
def remove_dups(head):
    seen = {}
    cur = head
    while cur:
        if cur.data in seen:
            seen[cur.data] += 1
        else:
            seen[cur.data] = 1
        cur = cur.next
    cur = head
    cur_next = cur.next
    while cur_next:
        if seen[cur_next.data] > 1:
            seen[cur_next.data] -= 1
            cur.next = cur_next.next
        else:
            cur = cur_next
        cur_next = cur_next.next
    return head


head = SinglyLinkedListNode.linkify([3, 3, 2, 2, 1, 4, 1])
print(head)
print(remove_dups(head))