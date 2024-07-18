class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numBottlesDrunk = 0
        leftOver = 0
        numFilledBottles = numBottles
        while numFilledBottles != 0:
            numBottlesDrunk += numFilledBottles
            numEmptyBottles = numFilledBottles + leftOver
            leftOver = numEmptyBottles % numExchange
            numFilledBottles = numEmptyBottles // numExchange
        return numBottlesDrunk