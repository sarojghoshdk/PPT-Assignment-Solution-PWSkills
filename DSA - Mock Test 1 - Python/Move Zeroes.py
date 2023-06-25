'''Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
a. 1 <= nums.length <= 10^4
b. -2^31 <= nums[i] <= 2^31 - 1'''

# Time Complexity = O(n)
# Space Complexity = O(1)
def moveZeroes(nums):
        n=len(nums)
        for i in range(0,n):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
        return nums

nums = [0,1,0,3,12]
x = moveZeroes(nums)
print(x)