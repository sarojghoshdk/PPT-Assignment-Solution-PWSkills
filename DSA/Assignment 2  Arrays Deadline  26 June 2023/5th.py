'''Question 5
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6'''

def maximumProduct(nums):
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
        # here (nums[0]*nums[1]*nums[-1]) is used because without it for some example
        # code given wronge output. for example:- nums = [-100,-98,-1,2,3,4] in this case 
        # actual output is 39200 but the code give the result 24.

nums = [1,2,3]
x = maximumProduct(nums)
print(x)