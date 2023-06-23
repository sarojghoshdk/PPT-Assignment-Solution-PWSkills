'''Question 6
Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1'''

def singleNumber(nums):
        xor = 0
        for num in nums:
            xor = xor ^ num
        
        return xor

nums = [2,2,1]
x = singleNumber(nums)
print(x)