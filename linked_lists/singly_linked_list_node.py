class SinglyLinkedListNode:
    def __init__(self, d):
        self.data = d
        self.next = None

    def __str__(self):
        lst = []
        cur = self
        while cur:
            lst.append(str(cur.data))
            cur = cur.next
        return "".join(lst)
    
    def ith_node(self, i):
        cur = self
        while cur:
            if i == 0:
                return cur
            i -= 1
            cur = cur.next

    @staticmethod
    def linkify(arr):
        head = SinglyLinkedListNode(arr[0])
        cur = head

        for elem in arr[1:]:
            cur.next = SinglyLinkedListNode(elem)
            cur = cur.next

        return head

