'''Question 2
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
           ● 0 <= a, b, c, d < n
           ● a, b, c, and d are distinct.
           ● nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]'''

def fourSum(nums , target):
        ans = set()      # here take empty set because if there is duplicate value then it take single value
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                left,right = j+1,len(nums)-1
                while left<right:
                    s = nums[i]+nums[j]+nums[left]+nums[right]
                    if s == target:
                        ans.add((nums[i],nums[j],nums[left],nums[right]))
                        right-=1
                        left+=1
                    elif s > target:
                        right-=1
                    else:
                        left+=1
                  
        return list(ans)

nums = [1,0,-1,0,-2,2]
target = 0
x = fourSum(nums,target)
print(x)