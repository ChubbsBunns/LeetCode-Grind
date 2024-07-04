class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        def printSubStr(st, low, high):
            print ((st[low: high + 1]))
        maxLength = 1
        length = len(s)
        start = 0
        
        for i in range(length):

            low = i - 1
            high = i
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > maxLength:

                    maxLength = high - low + 1
                    start = low
                low -= 1
                high += 1
            

            low = i - 1
            high = i + 1
            while (low >= 0 and high < length and s[low] == s[high]):
                if high - low + 1 > maxLength:

                    maxLength = high - low + 1
                    start = low
                low -= 1
                high += 1
            
        substringAns = s[start: start + maxLength]

solution = Solution
thing = solution.longestPalindrome(solution, "aaacbabdbabc")