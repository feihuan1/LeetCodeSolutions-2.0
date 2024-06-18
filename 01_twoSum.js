// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

var twoSum = function(nums, target) {
    const obj = {} 

    for(let i = 0; i < nums.length; i++){
        const toTarget = target - nums[i]; 

        if(obj.hasOwnProperty(toTarget)) {
            return [obj[toTarget], i]
        } else {
            obj[nums[i]] = i
        }
    }

    return -1
}