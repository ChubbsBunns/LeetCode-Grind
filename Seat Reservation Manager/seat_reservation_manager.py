import heapq

class SeatManager:

    def __init__(self, n: int):
        initialList = list(range(1, n + 1))
        heapq.heapify(initialList)  # Create the heap from the list
        self.heap = initialList

    def reserve(self) -> int:
        return heapq.heappop(self.heap)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
        
