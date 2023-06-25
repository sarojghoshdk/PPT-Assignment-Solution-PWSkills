'''<aside>
💡 **Question 2**
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

Given the integer n, return *the number of **complete rows** of the staircase you will build*.

**Example 1:**

[]()

![v2.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bd91cfa-d2b1-47b3-8197-a72e8dcfff4b/v2.jpg)

**Input:** n = 5

**Output:** 2

**Explanation:** Because the 3rd row is incomplete, we return 2.'''

# TC = O(1)
# SC = O(1)
def arrangeCoins(n):
        return (int)((2 * n + 0.25)**0.5 - 0.5)

n = 5
x = arrangeCoins(n)
print(x)


# TC = O(logn)
# SC = O(1)
# Another approach (Binary Search)
'''def arrangeCoins(n):
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right

n = 5
x = arrangeCoins(n)
print(x)'''