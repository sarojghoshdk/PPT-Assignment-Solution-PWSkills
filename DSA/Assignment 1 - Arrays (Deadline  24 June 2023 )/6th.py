'''**Q6.** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

Output: true'''

def containsDuplicate(nums):
	return len(set(nums)) != len(nums)

nums = [1,2,3,1]
x = containsDuplicate(nums)
print(x)