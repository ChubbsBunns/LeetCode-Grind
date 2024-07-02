from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buy = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > buy:
                if (prices[i] - buy) > maxProfit:
                    maxProfit = prices[i] - buy
        if maxProfit < 0:
            return 0 
        return maxProfit


solution = Solution
prices = [7,6,4,3,1]
ans = solution.maxProfit(solution, prices)
print(ans)