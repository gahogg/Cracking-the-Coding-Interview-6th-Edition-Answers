# You have two numbers represented by a linked list, where each
# node contains a single digit. The digits are stored in reverse order,
# such that the 1's digits is at the head of the list. Write a function
# that adds the two numbers and returns the sum as a linked list.
from singly_linked_list_node import SinglyLinkedListNode


# O(n) time, O(1) space
def sum_lists(head1, head2):
    exponent = 0
    sum_so_far = 0

    while head1 or head2:
        if head1:
            sum_so_far += head1.data * 10 ** exponent
            head1 = head1.next
        if head2:
            sum_so_far += head2.data * 10 ** exponent
            head2 = head2.next
        exponent += 1
    
    return sum_so_far



head1 = SinglyLinkedListNode.linkify([3, 2, 4, 2, 1])
head2 = SinglyLinkedListNode.linkify([3, 2])
print(sum_lists(head1, head2))