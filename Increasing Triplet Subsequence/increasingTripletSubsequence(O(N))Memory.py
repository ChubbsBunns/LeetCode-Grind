
from typing import List
from collections import deque

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smaller = deque([-1])
        bigger = deque([-1])
        smallest = nums[0]
        biggest = nums[len(nums) - 1]
        smallerIndex = 0
        biggerIndex = len(nums) - 1
        for i in range(1, len(nums)):
            if (nums[i] > smallest):
                smaller.append(smallerIndex)
            else:
                smallerIndex = i
                smallest = nums[i]
                smaller.append(-1)

        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] < biggest):
                bigger.appendleft(biggerIndex)
            else:
                biggest = nums[i]
                biggerIndex = i
                bigger.appendleft(-1)
        smaller = list(smaller)
        bigger = list(bigger)

        for i in range(len(nums)):
            if (smaller[i] != -1 and bigger[i] != -1):
                return True
        return False        