class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n).replace('0', '')[1:]
        return len(binary)
    
solution = Solution
print(solution.hammingWeight(solution, 11))