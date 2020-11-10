import numpy as np 

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        """
        # The algorithm:
        #       1. rotate every array
        #                v        v       v        v  
        #     -> [11,9,1,5],[10,8,4,2],[7,6,3,13],[16,12,14,15]
        #       
        #        2. swap first 3 elements of the 1 array with every 1st backwards of the other 3 arrays
        #         v  v  v v        v v     v   v   v        v   
        #     -> [15,13,2,5],[10,8,4,1],[7,6,3,9],[16,12,14,11]
        #
        #        3. swap first 2 elements of the 2 array with every 2rd backwards of last 2 arrays 
        #         v  v  v v   v  v v v     v v v   v     v  v   
        #     -> [15,13,2,5],[14,3,4,1],[7,6,8,9],[16,12,10,11]
        #         
        #        4. swap swap the 1 elemnt of the 3 array with the 3rd backwards of the last 1 array
        #         v  v  v v   v  v v v   v v v v   v  v  v  v   
        #     -> [15,13,2,5],[14,3,4,1],[7,6,8,9],[16,12,10,11]

        # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        # Output: [[7,4,1],[8,5,2],[9,6,3]]

        #      v     v     v 
        # [3,2,1],[6,5,4],[9,8,7]
        #  v v v     v v   v   v
        # [7,4,1],[6,5,2],[9,8,3]
        #  v v v   v v v   v v v
        # [7,4,1],[8,5,2],[9,6,3]

        n = len(matrix)

        # rotate every array
        for i in range(n):
            matrix[i] = matrix[i][::-1]

        # begin swaping
        for i in range(n-1):
            for j in range(n-i-1):
                matrix[i][j], matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1], matrix[i][j] 

        return matrix

    def rotate2(self, matrix) -> None:
        matrix = np.array(matrix)
        return matrix @ np.array([[0, 1],[-1, 0]])


matrix = [[1,2,3],[4,5,6],[7,8,9]]

s = Solution()
print(s.rotate2(matrix))
