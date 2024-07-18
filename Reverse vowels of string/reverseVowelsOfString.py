class Solution:
    def reverseVowels(self, s: str) -> str:
        leftIndex = 0
        rightIndex = len(s) - 1
        vowels = set(['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'])
        ans = []
        for character in s:
            ans.append(character)
        while leftIndex != rightIndex and leftIndex < rightIndex:
            while (s[leftIndex] not in vowels and leftIndex < rightIndex):
                leftIndex += 1
                if (leftIndex == len(s)):
                    break
            while (s[rightIndex] not in vowels and rightIndex > leftIndex):
                rightIndex -= 1
                if (rightIndex == -1):
                    break
            temp = ans[leftIndex]
            ans[leftIndex] = ans[rightIndex]
            ans[rightIndex] = temp
            leftIndex += 1
            rightIndex -= 1
        stringAns = ""
        for i in range(len(ans)):
            stringAns += ans[i]
        return stringAns