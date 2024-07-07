from typing import List
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coinChangeUtil(coins: List[int], amount: int, minCoinTable) -> int:
            if amount == 0:
                return 0
            
            if minCoinTable[amount] != -1:
                return minCoinTable[amount]
            
            res = sys.maxsize

            for coin in coins:
                if coin <= amount:
                    subRes = coinChangeUtil(coins, amount - coin, minCoinTable)
                    if subRes != sys.maxsize and subRes + 1 < res:
                        res = subRes + 1    
            minCoinTable[amount] = res
            return res
        minCoinTable = [-1] * (amount + 1)
        return coinChangeUtil(coins, amount, minCoinTable)

solution = Solution
coins = [2]
amount = 11
ans = solution.coinChange(solution, coins, amount)
if (ans == sys.maxsize):
    print("-1")
else:
    print(ans)



