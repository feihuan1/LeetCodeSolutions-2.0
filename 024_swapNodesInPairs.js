// time: O(n)
// space: O(1)

class ListNode {
    constructor(val, next) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

var swapPairs = function(head) {
    const dummy = new ListNode(0, head) 
    let prev = dummy 
    let curr = head 

    //make sure there is a pair to swap
    while(curr && curr.next) {
        // save start of next pair and second node of current pair
        let nextPair = curr.next.next 
        let second = curr.next

        //reverse it-> 3 step 
        second.next = curr 
        curr.next = nextPair 
        prev.next = second 

        // move pointer update pairs 
        prev = curr 
        curr = nextPair
    }

    return dummy.next
};