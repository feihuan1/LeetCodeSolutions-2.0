// # Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.


// # 1. brute force Approach (noob)
// # time:  O((m+n)log(m+n))
// # space: O(m+n)
var findMedianSortedArrays = function(nums1, nums2) {
    const arr = [...nums1, ...nums2] 
    arr.sort((a, b) => a- b) 
    
    let mid = Math.floor(arr.length / 2)

    return arr.length % 2 === 0 ? (arr[mid - 1] + arr[mid]) / 2 : arr[mid]
};


// #2. binary search
// # time: O(log(min(m,n))) 
// # space : O(1)

// # swap num1 and num2 identify shorter list 
// # set 2 pointer and run binary search on short list 
// # updating pointer until find right half point on both list 
// # find 4 element of each side of both list in the middle
// # if list is odd , return min of right side element on two list 
// # if list is even, return max of leftside and min of right side of two list

var findMedianSortedArrays = function(nums1, nums2) {
    let a = nums1 
    let b = nums2 

    if(a.length > b.length) {
        [a, b] = [b, a]
    } 

    const total = a.length + b.length 

    const half = Math.floor(total / 2) 

    let l = 0 
    let r = a.length - 1 

    while(true) {
        let i = Math.floor((l + r) / 2)
        let j = half - i - 2

        let aLeft = i >= 0 ? a[i] : -Infinity 
        let aRight = (i + 1) < a.length ? a[i + 1] : Infinity 
        let bLeft = j >= 0 ? b[j] : -Infinity 
        let bRight = (j + 1) < b.length ? b[j + 1] : Infinity 

        if(aLeft <= bRight && bLeft <= aRight) {
            if(total % 2 === 1) {
                return Math.min(aRight, bRight)
            } else {
                return (Math.max(aLeft, bLeft) + Math.min(aRight, bRight)) / 2
            }
        } else if (aLeft > bRight) {
            r = i - 1
        } else {
            l = i + 1
        }
    }
};