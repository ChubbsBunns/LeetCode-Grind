class Solution:
    def fib(self, n: int) -> int:
        if n == 0 | 1:
            return n
        
        prev1 = 0
        prev2 = 1
        currAns = 0
        
        for i in range(2,n + 1):
            currAns = prev1 + prev2
            prev1 = prev2
            prev2 = currAns
        return currAns

solution = Solution
thing = solution.fib(solution, 5)