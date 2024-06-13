# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# def twoSum(nums, target):
#     dic = {}

#     for index in range(len(nums)):
#         needs = target - nums[index]

#         if needs in dic:
#             return [dic[needs], index]
#         else:
#             dic[nums[index]] = index

#     return -1


def twoSum(nums, target):
    dic = {}

    for index, num in enumerate(nums): 
        needs = target - num 

        if needs in dic:
            return [dic[needs], index]
        else:
            dic[num] = index
    
    return -1


nums = [2,7,11,15]
target = 9

res = twoSum(nums, target)

print(res)