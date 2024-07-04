from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        currIVal = None
        for i in range(len(nums) - 2):
            if nums[i] == currIVal:
                continue
            else:
                currIVal = nums[i]
            if currIVal == None:
                currIVal = nums[i]
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                val = nums[i] + nums[left] + nums[right]
                if (val == 0):
                    ans.append([nums[i], nums[left], nums[right]])
                if val < 0 or val== 0:
                    currLeft = nums[left]
                    while left < right:
                        left += 1
                        newLeft = nums[left]
                        if newLeft != currLeft:
                            break
                if val > 0 or val==0:
                    currRight = nums[right]
                    while right > left:
                        right -= 1
                        newRight = nums[right]
                        if (newRight != currRight):
                            break
        return ans

    
solution = Solution
input = [0,0,0]
print(solution.threeSum(solution, input))