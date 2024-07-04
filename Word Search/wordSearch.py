from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def checkForWord(board: List[List[str]], word: str, xIndex: int, yIndex: int, table: set, height: int, width: int, currentIndex):
            if currentIndex == len(word) - 1:
                return True
            # check top
            if xIndex != 0:
                if board[xIndex - 1][yIndex] == word[currentIndex + 1] and (xIndex - 1, yIndex) not in table:
                    currentIndex += 1
                    xIndex -= 1
                    table.add((xIndex, yIndex))
                    if checkForWord(board, word, xIndex, yIndex, table, height, width, currentIndex):
                        return True
                    else:
                        table.remove((xIndex, yIndex))
                        currentIndex -=1
                        xIndex += 1
            # Check bottom
            if xIndex != height - 1:
                if board[xIndex + 1][yIndex] == word[currentIndex + 1] and (xIndex + 1, yIndex) not in table:
                    currentIndex += 1
                    xIndex += 1
                    table.add((xIndex, yIndex))
                    if checkForWord(board, word, xIndex, yIndex, table, height, width, currentIndex):
                        return True
                    else:
                        table.remove((xIndex, yIndex))                        
                        xIndex -= 1
                        currentIndex -=1
            # Check left
            if yIndex != 0:
                if board[xIndex][yIndex - 1] == word[currentIndex + 1] and (xIndex, yIndex - 1) not in table:
                    currentIndex += 1
                    yIndex -= 1
                    table.add((xIndex, yIndex))
                    if checkForWord(board, word, xIndex, yIndex, table, height, width, currentIndex):
                        return True
                    else:
                        table.remove((xIndex, yIndex))
                        yIndex += 1
                        currentIndex -= 1
            # Check right
            if yIndex != width - 1:
                if board[xIndex][yIndex + 1] == word[currentIndex + 1] and (xIndex, yIndex + 1) not in table:
                    currentIndex += 1
                    yIndex += 1
                    table.add((xIndex, yIndex))
                    if checkForWord(board, word, xIndex, yIndex, table, height, width, currentIndex):
                        return True
                    else:
                        table.remove((xIndex, yIndex))
                        currentIndex -= 1
                        yIndex -= 1
                        
            return False

        height = len(board)
        width = len(board[0])
        for i in range(len(board)):
            for j in range(len(board[i])):
                currentIndex = 0
                table = set()
                if word[0] == board[i][j]:
                    table.add((i,j))
                    if checkForWord(board, word, i, j, table, height, width, currentIndex):
                        return True
        return False

    
solution = Solution
board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
print("Solution is:")
print(solution.exist(solution, board, word))
        
