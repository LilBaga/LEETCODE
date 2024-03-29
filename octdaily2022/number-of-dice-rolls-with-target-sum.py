#number-of-dice-rolls-with-target-sum link:https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
#Straight forward solution
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
         @lru_cache(maxsize=None)
         def dp(d, t):
            if d * f < t or t < d:
                return 0
            if d == 1:
                return 1 <= t <= f
            return sum(dp(d-1, t-i) for i in range(max(1, t-(d-1)*f), min(f+1, t)))
         return dp(d, target) % (10**9 + 7)
