from typing import List
import math
import sys


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()
        numbers.update(nums)
        maxLength = 0
        for num in numbers:
            currLength = 0
            if (num - 1 in numbers):
                continue
            if (num != sys.maxsize & num - 1 not in numbers ):

                for i in range(num, sys.maxsize):
                    if (i not in numbers):
                        break
                    currLength += 1
            if maxLength < currLength:
                maxLength = currLength
        return maxLength
        

solution = Solution

longest_sequence_length = solution.longestConsecutive(solution, [0,3,7,2,5,8,4,6,0,1])

print(f"Length of longest consecutive sequence: {longest_sequence_length}")