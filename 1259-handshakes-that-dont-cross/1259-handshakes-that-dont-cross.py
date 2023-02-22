def ways(n, mem):
    if n in mem:
        return mem[n]
    n_ways = 0
    for i in range(0,n-1,2):
        n_ways += ways(i,mem)*ways(n-i-2, mem)
    mem[n] = n_ways
    return n_ways
class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        dp = {2 : 1, 0:1}
        return ways(numPeople, dp)%(10**9 + 7)