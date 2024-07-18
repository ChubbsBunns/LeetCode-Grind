class Solution:
    def minOperations(self, logs: List[str]) -> int:
        numOperations = 0
        for log in logs:
            if log == "../":
                if numOperations == 0:
                    continue
                else:
                    numOperations -= 1
                    continue
            if log == "./":
                continue
            if log != "../" and log !="./":
                numOperations += 1
        return numOperations