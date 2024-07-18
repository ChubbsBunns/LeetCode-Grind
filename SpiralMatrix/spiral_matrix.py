from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])

        ringIndex = 0

        ans = []
        while height > 0 and width > 0:
            topLeftIndex = ringIndex
            widthMaxIndex = ringIndex + width - 1
            heightMaxIndex = ringIndex + height - 1
            for i in range(ringIndex, widthMaxIndex + 1):
                ans.append(matrix[ringIndex][i])
            print("Top side is: ")
            print(ans)
            for i in range(ringIndex + 1, heightMaxIndex + 1):
                ans.append(matrix[i][widthMaxIndex])

            for i in range(widthMaxIndex - 1, ringIndex - 1, - 1):
                ans.append(matrix[heightMaxIndex][i])
            
            for i in range(heightMaxIndex - 1, ringIndex, -1):
                ans.append(matrix[i][ringIndex])
            
            ringIndex += 1
            width -= 2
            height -= 2
            print("Ans is now ")
            print(ans)
            print("Width is " + str(width))
            print("Height is" + str(height))
        return ans

solution = Solution
print(solution.spiralOrder(solution, [[2,5,8],[4,0,-1]]))
