# Implement a function to check if a linked list is a palindrome.
from singly_linked_list_node import SinglyLinkedListNode
from collections import deque


# O(n) runtime, O(n) space
def is_palindrome(head):
    deq = deque()
    while head:
        deq.append(head.data)
        head = head.next
    while deq:
        if len(deq) == 1:
            return True
        else:
            right = deq.pop()
            left = deq.popleft()
            if left != right:
                return False
    return True

# Trues
head1 = SinglyLinkedListNode.linkify(['a', 'a', 'b', 'b', 'b', 'a', 'a'])
head2 = SinglyLinkedListNode.linkify(['a', 'a', 'b', 'b', 'a', 'a'])
head3 = SinglyLinkedListNode.linkify(['a', 'a', 'b', 'a', 'a'])
head4 = SinglyLinkedListNode.linkify(['a']) 

# Falses
head5 = SinglyLinkedListNode.linkify(['a', 'b']) 
head6 = SinglyLinkedListNode.linkify(['a', 'b', 'c']) 
head7 = SinglyLinkedListNode.linkify(['c', 'a', 'd', 'b', 'a', 'c']) 
head8 = SinglyLinkedListNode.linkify(['c', 'a', 'd', 'c']) 

print(list(map(is_palindrome, [head1, head2, head3, head4, head5, head6, head7, head8])))

