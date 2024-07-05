//create dummy node , assign head to it's next 
// set first and second pointer 
// move first n times
// move first and second til first reach end of list 
// remove second.next 
// return dummy.next

// time:O(n) 
// space: O(1)

class Listnode{
    constructor(val){
        this.val = val 
        this.next = null
    }
}

var removeNthFromEnd = function(head, n) {
    const dummy = new ListNode(0) 
    dummy.next = head 
    let first = dummy
    let second = dummy 

    for(let i = 0; i<n; i++) {
        first = first.next
    } 

    while(first.next !== null) {
        first = first.next 
        second = second.next
    } 

    second.next = second.next.next 

    return dummy.next

};