class Solution:
    def reverseWords(self, s: str) -> str:
        filteredString = ""
        start = True
        space = False
        for index in range(len(s)):
            if s[index] != " ":
                start = False
                space = False
                filteredString += s[index]
            if (s[index]) == " " and start:
                continue
            if (s[index] == " "):
                filteredString += s[index]
                space = True
        filteredString = filteredString.rstrip()
            
        index = len(s)
        ans =""
        for index in range(len(filteredString) -1, -1, -1):
            if (filteredString[index] == " " or index == 0):
                currWordIndex = 0
                setSpace = False
                isMultipleSpace = True
                if (index != 0):
                    currWordIndex = index + 1
                    setSpace = True
                while filteredString[currWordIndex] != " " or currWordIndex != (len(filteredString) - 1):
                    if (filteredString[currWordIndex] == " "):
                        break    
                    isMultipleSpace = False
                    ans += filteredString[currWordIndex]
                    currWordIndex += 1
                    if (currWordIndex >= len(filteredString)):
                        break
                if (setSpace and isMultipleSpace == False):
                    ans += " "
        return ans

        