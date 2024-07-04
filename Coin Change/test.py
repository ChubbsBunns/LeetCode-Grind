from typing import List
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoinTable = [-1]*(amount + 1)
        def coinChangeUtil(coins: List[int], amount: int, minCoinTable) -> int:
            if amount == 0:
                return 0
            if minCoinTable[amount] != -1:
                return minCoinTable[amount]

            res = sys.maxsize
            for coin in coins:
                if coin <= amount:
                    subRes = coinChangeUtil(coins, amount - coin, minCoinTable)
                    if subRes != sys.maxsize and subRes < res:
                        subRes += 1
                        res = subRes
                
            minCoinTable[amount] = res
            return res

        ans = coinChangeUtil(coins, amount, minCoinTable)
        if ans == sys.maxsize:
            return -1
        return ans

solution = Solution
coins = [1,2]
amount = 11
print(solution.coinChange(solution, coins, amount))