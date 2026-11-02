class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[i] = 凑出金额 i 所需的最少硬币数
        dp = [inf]*(1+amount)
        dp[0] = 0
        for i in range(1,1+amount):
            for coin in coins:
                if coin > i:
                    continue
                dp[i] = min(dp[i],dp[i - coin] + 1)
        return -1 if inf == dp[amount] else dp[amount]  