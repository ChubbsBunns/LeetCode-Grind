class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n:
            return time + 1
        length_per_pass = n - 1
        index = time % length_per_pass
        num_passes = time/length_per_pass
        if (int(num_passes) % 2  == 0) :
            return 1 + index
        else:
            return n - index