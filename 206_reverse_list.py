from typing import Optional

# // super simple 3 step 
# // 1 set prev null and curr is head 
# // loop while curr is in bound 
# // save curr.next and change pointer to prev then update prev to curr and curr to curr.next

# //Time : O(n)
# //Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head 

        while curr: 
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
        return prev