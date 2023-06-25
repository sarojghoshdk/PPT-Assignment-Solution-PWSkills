'''<aside>
💡 **Question 7**

Suppose an array of length n sorted in ascending order is **rotated** between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that **rotating** an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in O(log n) time.

**Example 1:**

**Input:** nums = [3,4,5,1,2]

**Output:** 1

**Explanation:**

The original array was [1,2,3,4,5] rotated 3 times.

</aside>'''

def findMin(nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            # if mid is greater than r then right part is rotated so search for
            # min in right part
            if nums[mid] > nums[right]:
                left = mid +1
            # mid is small than rightmost ele so min should be in left part
            #search in left part for min element 
            else: 
                right = mid 
        #return leftmost min number 
        return nums[left]    

nums = [3,4,5,1,2]
x = findMin(nums)
print(x)
