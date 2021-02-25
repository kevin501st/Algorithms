class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    position = 1
    start = head
    while position < m - 1:
        start = start.next
        position += 1

    while position < n:
        m_node = start.next
        next_node = m_node.next
        temp = m_node.next.next
        start.next = next_node
        m_node.next.next = m_node
        m_node.next = temp
        position += 1

    return head


linked = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

l = reverseBetween(linked, 2, 4)