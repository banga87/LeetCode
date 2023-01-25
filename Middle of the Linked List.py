"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(self, head: ListNode) -> ListNode:
    count = 0
    full = head
    half = head
    while full:
        count += 1
        full = full.next
        if count % 2 == 0:
            half = half.next
    return half