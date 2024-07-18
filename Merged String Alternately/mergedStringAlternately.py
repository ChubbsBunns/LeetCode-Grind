class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ""
        length = 0
        otherLength = 0
        if len(word1) > len(word2):
            length = len(word2)
            otherLength = len(word1)
        else:
            length = len(word1)
            otherLength = len(word2)
        
        for i in range(length):
            mergedString = mergedString + word1[i] + word2[i]
        

        if (len(word1) == otherLength):
            for i in range(length, otherLength):
                mergedString = mergedString + word1[i]
        else:
            for i in range(length, otherLength):
                mergedString = mergedString + word2[i]
        return mergedString

        