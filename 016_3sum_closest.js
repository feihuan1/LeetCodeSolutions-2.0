// sort array, set defaul res 
// loop array skip duplicates 
// set two pointer between next index and end  
// if sum equal target means distance is 0, return it, else, update res if sum is closer to target 
// move pointer depends if sum is too small or too big


// time O(n^2)
// space: O(log n)

var threeSumClosest = function(nums, target) {
    if(nums.length < 3) return null 

    let res = nums[0] + nums[1] + nums[2]  
    nums.sort((a,b) => a-b)

    for( let i = 0; i < nums.length; i++){
        if ( i> 0 && nums[i] === nums[i-1]) continue 

        let j = i + 1 
        let k = nums.length - 1 

        while(j < k) {
            const sum = nums[i] + nums[j] + nums[k]  

            if (sum === target) return sum 

            if(Math.abs(target - sum) < Math.abs(target - res)){
                res = sum
            } 

            if(sum < target){
                j ++
            } else {
                k--
            }
            
        }
    }
    return res
};