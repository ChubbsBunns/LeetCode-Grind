

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currLen = 0
        currentChars = set()
        maxLength = 0
        j = 1
        if len(s) <= 1:
            return len(s)
        if len(s) >= 2:
            currLen = 1
        i = 0
        currentChars.add(s[i])
        while (i < len(s) and j < len(s)):
            if (s[j] not in currentChars):
                currentChars.add(s[j])
                currLen += 1
                j += 1
            else:
                if (maxLength < currLen):
                    maxLength = currLen
                while (s[i] != s[j]):
                    if (i >= len(s) or j >= len(s)):
                        break
                    currentChars.remove(s[i])
                    i += 1
                    currLen -= 1
                i += 1
                j += 1
        if (maxLength < currLen):
            maxLength = currLen
        return maxLength


solution = Solution
something = solution.lengthOfLongestSubstring(solution, "ab")
print(something)