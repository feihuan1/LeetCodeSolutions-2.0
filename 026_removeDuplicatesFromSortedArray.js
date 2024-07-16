// # set two pointer to be 1 loop array(first element doesnt matter), right++ if duplicate with last element, else set nums[left] to be nums[right] and update both pointer 
// # return left pointer,(uniq element + 1), and array become uniq in beginning 

// #time: O(n)
// #space: O(1)

var removeDuplicates = function(nums) {
    if(nums.length <= 1) return nums.length 

    let curr = 1 
    for ( let i = 1; i < nums.length; i++) {
        if(nums[i] === nums[i - 1]) continue; 

        nums[curr] = nums[i] 
        curr ++
    } 
    return curr
};