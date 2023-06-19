'''**Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

Output: 2'''

def searchInsert(nums, target):
        start, end = 0, len(nums) - 1
        ans = len(nums) # Default answer when target is greater than all elements
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                ans = mid # Update the answer to the current index
                end = mid - 1
                
        return ans


nums = [1,3,5,6]
target = 5
x = searchInsert(nums,target)
print(x)