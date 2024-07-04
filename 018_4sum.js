// # sort input and use nested loop , i starts 0 ends len(nums)-4 , j starts i + 1 ends len(nums) - 3
// # set two pointer find two more digits add to nums at index of i and j to match the target, 
// # push to target or increment on of the pointer depends on the sum 
// # use while loop skip duplicates on each loop

// # time: O(n^3)
// # space: O(log n)