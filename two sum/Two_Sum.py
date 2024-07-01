from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            
            diff = target - num
            if (diff in nums and diff in seen):
                if (seen[diff] != i):
                    return [seen[diff], i]
            seen[num] = i    
        return []
    
solution = Solution
something = (solution.twoSum(solution, [2,15,11,7], 9))
print(something)
if len(something) == 0:
    print("someting wong")
