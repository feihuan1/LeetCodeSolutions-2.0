# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.


# 1. brute force Approach (noob)
# time:  O((m+n)log(m+n))
# space: O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        new = nums1 + nums2 
        new.sort()
        mid = len(new) // 2
        if len(new) % 2 == 0:
            return (new[mid] + new[mid - 1]) / 2
        else:
            return new[mid]

#2. binary search
# time: O(log(min(m,n))) 
# space : O(1)

# swap num1 and num2 identify shorter list 
# set 2 pointer and run binary search on short list 
# updating pointer until find right half point on both list 
# find 4 element of each side of both list in the middle
# if list is odd , return min of right side element on two list 
# if list is even, return max of leftside and min of right side of two list

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        a, b = nums1, nums2 
        total = len(a) + len(b) # total lenth
        half = total // 2 # half lenth,

        # make sure a is the shorter list, swap if not
        if len(b) < len(a):
            a, b = b, a

        # run binary search on a(smaller list)
        l, r = 0, len(a) - 1 # these are index from 0 and lenth -1 of list a! 
        while True:  # break when find right index
            i = (l + r) // 2 # middle of list a (pointer for a ) 
            j = half - i - 2 # middle of list b (pointer for b)

            # find left and right element of middle on each list 
            a_left = a[i] if i >= 0 else float('-infinity') 
            a_right = a[i + 1] if (i + 1 )< len(a) else float('infinity')
            b_left = b[j] if j >= 0 else float('-infinity')
            b_right = b[j + 1] if (j + 1) < len(b) else float('infinity')

            # partition is correct 
            if a_left <= b_right and b_left <= a_right:
                #odd 
                if total % 2: # True==1 
                    return min(a_right, b_right) # if one is infinity, will take the non-infinity number
                # even 
                else: 
                    # max left and min right is the middle two number
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            # too many elements in list a half
            elif a_left > b_right:
                # reducing half point of a by moving right pointer
                r = i - 1
            else: # b_left > a_right -> too many elements in b list half
                l = i + 1