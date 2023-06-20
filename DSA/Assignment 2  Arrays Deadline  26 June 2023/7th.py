'''Question 7
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true'''

def isMonotonic(nums):
        increasing = decreasing = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                increasing = False
            if nums[i] < nums[i+1]:
                decreasing = False

        return increasing or decreasing

nums = [1,2,2,3]
x = isMonotonic(nums)
print(x)