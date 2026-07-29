class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # Step 1: Check if there are at least k nodes remaining
        node = head
        count = 0
        while node and count < k:
            node = node.next
            count += 1
        
        if count < k:
            # Fewer than k nodes left — leave them as-is
            return head
        
        # Step 2: Reverse the first k nodes
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: head is now the tail of this reversed group.
        # Recursively reverse the rest, and connect it.
        head.next = self.reverseKGroup(curr, k)
        
        return prev  # prev is now the new head of this group