class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append([v, t])
            graph[v].append([u, t])

        def dijkstra(src):
            dist = [math.inf] * n
            ways = [0] * n
            minHeap = [(0, src)]  # dist, src
            dist[src] = 0
            ways[src] = 1
            while minHeap:
                d, u = heappop(minHeap)
                if dist[u] < d: continue  # Skip if d is not updated to latest version!
                for v, t in graph[u]:
                    if dist[v] > d + t:
                        dist[v] = d + t
                        ways[v] = ways[u]
                        heappush(minHeap, (dist[v], v))
                    elif dist[v] == d + t:
                        ways[v] = (ways[v] + ways[u]) % 1000000007
            return ways[n - 1]

        return dijkstra(0)