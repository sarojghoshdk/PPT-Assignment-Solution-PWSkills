'''<aside>
💡 **Question 3**
Given a 2D integer array matrix, return *the **transpose** of* matrix.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

**Example 1:**

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [[1,4,7],[2,5,8],[3,6,9]]

</aside>'''

def transpose(matrix):
        row = len(matrix)
        column = len(matrix[0])
        
        result = [[None] * row for _ in range(column)]

        for r in range(row):
            for c in range(column):
                result[c][r] = matrix[r][c]

        return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
x = transpose(matrix)
print(x)