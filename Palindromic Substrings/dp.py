class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        table = [[0 for x in range(length) ] for y in range(length)]
        ans = 0
        for i in range(length):
            table[i][i] = True
            ans += 1

        for i in range(1, length):
            if s[i - 1] == s[i]:
                table[i - 1][i] = True
                ans += 1
        
        k = 3
        while k < length + 1:
            i = 0
        # Set all characters that are palindromes of length 3 and more
            while i < (len(s) - k + 1):
                j = i + k - 1
                if (s[i] == s[j] and table[i + 1][j - 1]):
                    table[i][j] = True
                    ans += 1
                i += 1
            k += 1
        return ans