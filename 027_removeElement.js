// two pointer loop nums, if current element  != val, move it to curr pointer, increment curr, return curr after loop

//time:O(n)
//space:O(1)

var removeElement = function(nums, val) {
    let curr = 0 
    for( let i = 0; i < nums.length; i++) {
        if(nums[i] !== val) {
            nums[curr] = nums[i] 
            curr ++
        } 
    }
    return curr
};