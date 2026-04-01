import heapq

class KthLargest:

    @property
    def maxHeap(self):
        return self._maxHeap

    @property
    def k(self):
        return self._k

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        
        # Max heap (in python heap is min by default, so using negative numbers for max heap)
        self._maxHeap = []
        for num in nums:
            heapq.heappush(self._maxHeap, num)

        # Keep only k largest elements
        while len(self._maxHeap) > k:
            heapq.heappop(self._maxHeap)

    def add(self, val: int) -> int:
        if len(self._maxHeap) < self.k:
            heapq.heappush(self._maxHeap, val)
        elif val > self._maxHeap[0]:
            heapq.heapreplace(self._maxHeap, val)

        return self._maxHeap[0]  # Root is kth largest
