class Solution:

    def compress(self, chars: List[str]) -> int:
        i = 0
        write = 0
        while i < len(chars):
            currChar = chars[i]
            count = 0
            while (i < len(chars) and chars[i] == currChar):
                count += 1
                i += 1
            chars[write] = currChar
            write += 1
            if count > 1:
                start = write
                length = 0
                while (count > 0):
                    toWrite = count%10
                    count = int(count/10)
                    chars[write] = str(toWrite)
                    length += 1
                    write += 1
                end = start + length - 1
                while (start < end):
                    temp = chars[end]
                    chars[end] = chars[start]
                    chars[start] = temp
                    start += 1
                    end -= 1

        return write
