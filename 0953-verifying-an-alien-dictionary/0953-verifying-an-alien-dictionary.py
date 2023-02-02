class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        arr = []
        for i in words:
            arr.append([order.index(j) for j in i])
        return arr == sorted(arr)
