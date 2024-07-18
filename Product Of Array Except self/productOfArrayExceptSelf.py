from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftToRight = [0]*len(nums)
        rightToLeft = [0]*len(nums)
        leftToRight[0] = (nums[0])
        rightToLeft[len(nums) - 1] = (nums[len(nums) - 1])
        for i in range(1,len(nums)):
            leftToRight[i] = (nums[i]*leftToRight[i-1])
        for i in range(len(nums) - 2, -1, -1):
            rightToLeft[i] = (nums[i]*rightToLeft[i + 1])
        ans = []
        ans.append(rightToLeft[1])
        for i in range(1,len(nums) - 1):
            ans.append(leftToRight[i - 1]*rightToLeft[i + 1])
        ans.append(leftToRight[len(nums) - 2])
        return ans
            