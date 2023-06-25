'''<aside>
💡 **Question 6**

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and 
each integer appears **once** or **twice**, return *an array of all the integers that appears **twice***.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

**Example 1:**

**Input:** nums = [4,3,2,7,8,2,3,1]

**Output:**

[2,3]'''

def findDuplicates(nums):
        ans = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return ans

nums = [4,3,2,7,8,2,3,1]
x = findDuplicates(nums)
print(x)