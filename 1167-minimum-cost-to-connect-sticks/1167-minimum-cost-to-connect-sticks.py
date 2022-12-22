class Solution:
    def connectSticks(self, A):
        heapq.heapify(A)
        res = 0
        while len(A) > 1:
            x, y = heapq.heappop(A), heapq.heappop(A)
            res += x + y
            heapq.heappush(A, x + y)
        return res