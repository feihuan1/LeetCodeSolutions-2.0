// super simple 3 step 
// 1 set prev null and curr is head 
// loop while curr is in bound 
// save curr.next and change pointer to prev then update prev to curr and curr to curr.next

//Time : O(n)
//Space: O(1)

class ListNode {
    constructor(val, next) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


var reverseList = function(head) {
    let prev = null 
    let curr = head 

    while(curr) {
        const nxt = curr.next 
        curr.next = prev 
        prev = curr 
        curr = nxt 
    }

    return prev
};