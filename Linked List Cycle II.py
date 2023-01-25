"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add_node(self, node):
        self.next = node


def detectCycle(head: ListNode) -> ListNode:
    slow, fast = head, head

    # First while loop finds when the loop begins
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            # Second while loop confirms the interesecting node
            while slow != fast:
                slow = slow.next
                fast = fast.next
            # Breaks out when the intersect is found
            return slow



