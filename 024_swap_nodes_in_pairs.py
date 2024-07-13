from typing import Optional

# // time: O(n)
# // space: O(1)



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        prev, curr = dummy, head 

        # make sure there is a pair to swap
        while curr and curr.next:
            # save start of next pair and second node of current pair
            next_pair = curr.next.next
            second = curr.next
            # reverse it-> 3 step  
            second.next = curr 
            curr.next = next_pair 
            prev.next = second
            # move pointer update pairs 
            prev = curr 
            curr = next_pair 
        
        return dummy.next