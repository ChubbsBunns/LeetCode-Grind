class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        def printSubStr(st, low, high):
            print ((st[low: high + 1]))
        maxLength = 1
        length = len(s)
        start = 0
        
        for i in range(length):
            #find substring of even length
            low = i - 1
            high = i
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > maxLength:
                    print("Start index is " + str(low))
                    print("End index is " + str(high))
                    print("Low val is " + str(s[low]))
                    print("High val is " + str(s[high]))
                    maxLength = high - low + 1
                    start = low
                low -= 1
                high += 1
            
            #find substring of odd length
            low = i - 1
            high = i + 1
            while (low >= 0 and high < length and s[low] == s[high]):
                if high - low + 1 > maxLength:
                    print("start index is " + str(low))
                    print("End index is " + str(high))
                    print("Low val is " + str(s[low]))
                    print("High val is " + str(s[high]))
                    maxLength = high - low + 1
                    start = low
                low -= 1
                high += 1
            
        print(start)
        print(maxLength)
        substringAns = s[start: start + maxLength]
        print("MaxLength is " + str(maxLength))
        print(substringAns)
solution = Solution
thing = solution.longestPalindrome(solution, "aaacbabdbabc")