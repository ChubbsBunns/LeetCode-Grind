from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        freq_table = {}
        for num in nums:
            if num in freq_table:
                freq_table[num] += 1
            else:
                freq_table[num] = 1

        count = 0
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num1 = nums[i]
                num2 = nums[j]
                freq_table[num1] -= 1
                freq_table[num2] -= 1
                lastRequiredNum = 0 - num1 - num2
                if lastRequiredNum in freq_table:
                    if freq_table[lastRequiredNum] != 0:
                        count += freq_table[lastRequiredNum]
                        ans.append([num1, num2, lastRequiredNum])
                freq_table[num1] += 1
                freq_table[num2] += 1
        
        print(ans)
        for triplet in ans:
            triplet.sort()
        ans.sort()

        ansList = []
        lastIndex = None
        for triplet in ans:
            if triplet != lastIndex:
                lastIndex = triplet
                ansList.append(triplet)
        
        return ansList
    
solution = Solution
input = [-1,0,1,2,-1,-4]
print(solution.threeSum(solution, input))