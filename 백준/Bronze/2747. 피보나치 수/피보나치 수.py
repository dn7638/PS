# dfs : n과m 다 풀고 14888 2580 1987
# bfs : 7562 7576 1697 13459
# dp : 2747 9095 11726 11051 1149 2156 9251 11049
# 다잌 : 1916 1504 12763  1854

n = int(input())
dp = [0 for _ in range(46)]
dp[1] = 1

for i in range(2,46):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])


