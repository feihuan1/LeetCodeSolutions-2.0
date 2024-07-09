// # while lists length is greater than 1
// # loop lists skip one index at time 
// # merge lists[i] and list[i+1] append to new lists 
// # lists = newLists 
// # when exist both loop, return lists[0]

// # time: O(NlogK) 
// # space: O(k)

class ListNode {
    constructor(val, next) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

var mergeKLists = function(lists) {
    if (lists.length === 0) return null 

    while(lists.length > 1) {
        let arr = [] 
        for(let i = 0; i < lists.length; i+=2) {
            const l1 = lists[i]
            const l2 = lists[i+1] 

            arr.push(mergeTwo(l1, l2))
        }
        lists = arr
    }
    return lists[0]
};

function mergeTwo(l1, l2){
    const dummy = new ListNode() 
    let tail = dummy 

    while(l1 && l2) {
        if(l1.val <= l2.val) {
            tail.next = l1 
            l1 = l1.next
        } else {
            tail.next = l2 
            l2 = l2.next
        }
        tail = tail.next
    }

    if(l1) tail.next = l1 
    if(l2) tail.next = l2 

    return dummy.next   

}