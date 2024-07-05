# //create dummy node , assign head to it's next 
# // set first and second pointer 
# // move first n times
# // move first and second til first reach end of list 
# // remove second.next 
# // return dummy.next

# // time:O(n) 
# // space: O(1)

from typing import Optional

class ListNode: 
    def __init__(self, val=0, next = None) -> None:
        self.val = val 
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # next property is passed in!!!

        first, second = dummy, dummy 

        for i in range(n+1):
            first = first.next 
        
        while first is not None:
            first = first.next 
            second = second.next 
        
        second.next = second.next.next 

        return dummy.next