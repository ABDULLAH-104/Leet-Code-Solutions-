class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            
            # Rewire: prev -> second -> first -> (rest of list)
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move prev forward to prepare for the next pair
            prev = first
        
        return dummy.next