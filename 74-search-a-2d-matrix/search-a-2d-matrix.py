class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Convert 2D to 1D(in single list) using 
        #l1=[matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])) ]
        n= len(matrix) * len(matrix[0])
        l=0
        r= n-1
        for i in range(n):
            mid = (l+r)//2
            cur = matrix[mid//len(matrix[0])][mid%len(matrix[0])]
            if target == cur:
                return True
            elif target < cur:
                r= mid -1
            elif target > cur:
                l= mid +1
        return False