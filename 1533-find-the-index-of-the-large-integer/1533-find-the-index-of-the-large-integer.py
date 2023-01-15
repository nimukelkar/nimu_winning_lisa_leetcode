class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        lo, hi = 0, n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if (hi - lo + 1) % 2 == 0:
                compare = reader.compareSub(lo, mid, mid + 1, hi)
            else:
                compare = reader.compareSub(lo, mid, mid, hi)
            
            if compare < 0:
                lo = mid + 1
            else:
                hi = mid
                
        return lo