class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        list=[]
        while matrix:
            list+=matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    list.append(row.pop())
            if matrix:
                list+=matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    list.append(row.pop(0))
        
        return list