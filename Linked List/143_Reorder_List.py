# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondHalf = slow.next
        slow.next = None
        prev = None

        # Reverse second half
        while secondHalf:
            tmp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = tmp

        # Merge first half and reversed second half
        firstHalf, secondHalf = head, prev
        while secondHalf:
            tmp1,tmp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = tmp1
            firstHalf = tmp1
            secondHalf = tmp2




