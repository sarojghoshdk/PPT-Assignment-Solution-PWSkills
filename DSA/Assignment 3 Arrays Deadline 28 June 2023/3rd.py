'''
💡 **Question 3**
A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater
permutation of its integer. More formally, if all the permutations of the array are
sorted in one container according to their lexicographical order, then the next
permutation of that array is the permutation that follows it in the sorted container.

If such an arrangement is not possible, the array must be rearranged as the
lowest possible order (i.e., sorted in ascending order).

● For example, the next permutation of arr = [1,2,3] is [1,3,2].
● Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
● While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

**Example 1:**
Input: nums = [1,2,3]
Output: [1,3,2]'''

def nextPermutation(nums):
        n = len(nums)
        k, l = n - 2, n - 1
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1
        if k < 0:
            nums.reverse()
        else:
            while l > k and nums[l] <= nums[k]:
                l -= 1
            nums[k], nums[l] = nums[l], nums[k]
            nums[k + 1:n] = reversed(nums[k + 1:n])
        return nums

nums = [1,2,3]
x = nextPermutation(nums)
print(x)