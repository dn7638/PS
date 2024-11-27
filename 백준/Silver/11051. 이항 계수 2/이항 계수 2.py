# dfs : n과m 다 풀고 14888 2580 1987
# bfs : 7562 7576 1697 13459
# dp : 2747 9095 11726 11051 1149 2156 9251 11049
# 다잌 : 1916 1504 12763  1854

n, k = map(int, input().split(' '))

dp = [0 for _ in range(1001)]
dp[1] = 1

for i in range(2,1001):
    dp[i] = dp[i-1]*i
if k == 0 or n-k == 0:
    print(1)
else:
    print((dp[n] // dp[k] // dp[n-k]) % 10007)
