import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

M = int(input())

ask = [list(map(int, input().split())) for _ in range(M)]

dp = [[0]*(N) for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

# n = 7
for i in range(1, N):
    for j in range(N-i):
        if nums[i+j] != nums[j]:
            dp[i+j][j] = 0
        else:
            if i == 1:
                dp[i+j][j] = 1
            else:
                dp[i+j][j] = dp[i+j-1][j+1]
        

for start, end in ask:
    print(dp[end-1][start-1])
    