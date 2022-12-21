class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislike = [[] for _ in range(n)]
        for a, b in dislikes:
            dislike[a-1].append(b-1)
            dislike[b-1].append(a-1)

        groups = [0] * n
        for p in range(n):
            if groups[p] == 0:
                groups[p] = 1
                q = deque([p])
                while q: # bfs
                    a = q.pop()
                    for b in dislike[a]:
                        if groups[b] == 0:
                            groups[b] = 1 if groups[a] == 2 else 2
                            q.appendleft(b)
                        elif groups[a] == groups[b]:
                            return False
        return True