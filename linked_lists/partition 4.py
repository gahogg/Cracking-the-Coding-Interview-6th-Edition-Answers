# Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes
# greater than or equal to x. If x is contained within
# the list, the values of x can apppear anywhere in 
# the 'right' partition
from singly_linked_list_node import SinglyLinkedListNode


# O(n) runtime, O(n) space
def partition(head, x):
    stk_lower = []
    stk_higher = []

    # Put elements on respective stacks
    cur = head
    while cur:
        if cur.data < x:
            stk_lower.append(cur)
        else:
            stk_higher.append(cur)
        cur = cur.next

    # Join the elements < x together, and place at front if at least one exists
    low = None
    if stk_lower:
        low = stk_lower.pop()
        head = low
        while stk_lower:
            low.next = stk_lower.pop()
            low = low.next
            
        low.next = None
    
    # Join the elements >= x together
    if stk_higher:
        high = stk_higher.pop()
        if low is None:
            head = high
        else:
            low.next = high
        while stk_higher:
            high.next = stk_higher.pop()
            high = high.next
        high.next = None
    
    return head


head = SinglyLinkedListNode.linkify([3, 2, 4, 2, 1])
print(head)
print(partition(head, 3))