class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ageAndScore = list(zip(ages, scores))
        ageAndScore.sort(key = lambda x: (x[0], x[1]))
        dp = [0] * len(scores)
        ans = 0
        for i, (_, sc) in enumerate(ageAndScore):
            dp[i] = sc
            for j in range(i):
                if ageAndScore[j][1] <= sc and dp[j] + sc > dp[i]:
                    dp[i] = dp[j] + sc
            if dp[i] > ans: ans = dp[i]
        return ans