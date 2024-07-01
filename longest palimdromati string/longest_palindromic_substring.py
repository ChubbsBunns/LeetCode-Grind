class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        def printSubStr(st, low, high):
            print ((st[low: high + 1]))
        start = 0
        maxLength = 1
        result = [[0 for x in range (len(s))] for y in range(len(s))]
        for i in range(len(s)):
            result[i][i] = True
        
        for i in range(len(s) - 1):
            if (s[i] == s[i+1]):
                result[i][i + 1] = True
                maxLength = 2
                start = i
        k = 3
        while k <= len(s):

        # Fix the starting index
            i = 0
            while i < (len(s) - k + 1):

                # Get the ending index of
                # substring from starting
                # index i and length k
                j = i + k - 1

                # Checking for sub-string from
                # ith index to jth index if
                # st[i + 1] to st[(j-1)] is a
                # palindrome
                if (result[i + 1][j - 1] and
                        s[i] == s[j]):
                    result[i][j] = True
                    if (k > maxLength):
                        start = i
                        maxLength = k
                i = i + 1
            k = k + 1
        substringAns = s[start: start + maxLength]
        return substringAns
    
    

solution = Solution
thing = solution.longestPalindrome(solution, "babbabd")
print("I am a chicken")
print(thing)
print("I am a duck")
