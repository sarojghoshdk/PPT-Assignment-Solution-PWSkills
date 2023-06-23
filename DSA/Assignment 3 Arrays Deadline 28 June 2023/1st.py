'''Question 1
Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to the target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).'''

def threeSumClosest(nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2] # initialize closest sum
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right: # two-pointer approach
                sum = nums[i] + nums[left] + nums[right]
                if sum == target: # sum equals target, return immediately
                    return sum
                if sum < target:
                    left += 1
                else:
                    right -= 1
                if abs(sum - target) < abs(closest_sum - target): # update closest sum
                    closest_sum = sum
        return closest_sum

nums = [-1,2,1,-4]
target = 1
x = threeSumClosest(nums,target)
print(x)