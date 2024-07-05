
// set dummy and pointer 
// while list1 or list2 is not at end compare list1 and list val, link witch ever smaller to pointer.next and update the list, update the pointer no mather witch is linked
// link the rest of list1 or list2 to pointer 
// return dummy.next

// time: O(n)
// space: O(n)

var mergeTwoLists = function(list1, list2) {
    let dummy = new ListNode() 
    let pointer = dummy
    while(list1 && list2) {
        if(list1.val <= list2.val) {
            pointer.next = list1 
            list1 = list1.next
        } else { 
            pointer.next = list2 
            list2 = list2.next
        }
        pointer = pointer.next
    }

    if (list1){
        pointer.next = list1
    }
    if(list2){
        pointer.next = list2
    }

    return dummy.next
};