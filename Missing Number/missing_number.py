import sys
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalNum = 0
        for i in range(len(nums) + 1):
            totalNum = totalNum ^ i

        for i in range(len(nums)):
            print("Totalnum was " + str(totalNum))
            totalNum = totalNum ^ nums[i]
            print("totalNum is now " + str(totalNum))
        print("Total bin num is " + str(totalNum))
        return int(totalNum)
    
solution = Solution
print(solution.missingNumber(solution, [0,1,2,4,5]))
