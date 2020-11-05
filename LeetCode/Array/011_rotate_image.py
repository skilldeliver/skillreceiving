class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 5, 1, 9, 11, 10, 7, 16, 12, 14, 15, 13, 2
        # 15, 13, 2, 5, 1, 9, 11, 10, 7, 16, 12, 14
        l = len(matrix[0]) 

        if l % 2 == 0:
#        Input: matrix = [
#               [5,1,9,11],
#               [2,4,8,10],
#               [13,3,6,7],
#               [15,14,12,16]
#        ]
# 
#        Output: [
#               [15,13,2,5],
#               [14,3,4,1],
#               [12,6,8,9],
#               [16,7,10,11]]
			row = 0
			col = 0
       		unfoled = list()

        	for i in range(l):

matrix = [
          [5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]
       ]

s = Solution()
s.rotate(matrix)