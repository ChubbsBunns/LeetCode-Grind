from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if (len(flowerbed) == 1):
            if (n > 1):
                return False
            if (flowerbed[0] == 0 or n == 0):
                return True
            return False
        
        if (flowerbed[1] == 0 and flowerbed[0] == 0):
            n -= 1
            flowerbed[0] = 1

        for i in range(1,len(flowerbed) - 1):
            if (flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0):
                flowerbed[i] = 1
                n -= 1

        if (len(flowerbed) > 1):
            if (flowerbed[-2] == 0 and flowerbed[-1] == 0):
                n -= 1
        if n > 0:
            return False
        return True