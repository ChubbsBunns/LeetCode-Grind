from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # initialize an array of size 60 
        #| This array is used to keep track of each remainder value
        remainders = [0] * 61
        numPairs = 0
        for i in range(len(time)):
            numPairs += remainders[(60 - time[i] % 60) % 60]
            remainders[time[i] % 60] += 1

        return numPairs
    
solution = Solution
time = [30, 20, 150, 100, 40]
thing = solution.numPairsDivisibleBy60(solution, time)
print(thing)