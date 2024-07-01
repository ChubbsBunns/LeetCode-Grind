from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrixLength = len(matrix)
        length = int(len(matrix)/2) + 1
        for degreesFromOuterRing in range(length):
            temp1 = 0
            temp2 = 0
            for indexInArray in range(matrixLength - degreesFromOuterRing*2 - 1):
                topX = degreesFromOuterRing 
                topY = degreesFromOuterRing + indexInArray
                rightX = degreesFromOuterRing + indexInArray
                rightY = matrixLength - degreesFromOuterRing - 1
                bottomX = matrixLength - degreesFromOuterRing - 1
                bottomY = matrixLength - degreesFromOuterRing - indexInArray - 1
                leftX = matrixLength - degreesFromOuterRing - indexInArray - 1
                leftY = degreesFromOuterRing
            
                print(matrix)
                #Store top right
                temp1 = matrix[rightX][rightY]
                #Replace top right
                matrix[rightX][rightY] = matrix[topX][topY]
                # Store bottom right
                temp2 = matrix[bottomX][bottomY]
                #Replace bottom right
                matrix[bottomX][bottomY] = temp1
                #Store bottom left
                temp1 = matrix[leftX][leftY]
                #Replace bottom left
                matrix[leftX][leftY] = temp2
                #Replace top left
                matrix[topX][topY] = temp1
            


solution = Solution
solution.rotate(solution, [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])