class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        a = a & mask
        while b != 0:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry & mask
        return a


solution = Solution
print(solution.getSum(solution, -1, 1))