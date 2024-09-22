N, M, K = map(int, input().split(' '))

candy = [0]
candy.extend(list(map(int, input().split(' '))))
parent = [ i for i in range(N+1)]

def find(x):
    if x == parent[x]:
        return x
    else:        
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    p_x = find(x)
    p_y = find(y)

    if x < y:
        parent[p_y] = p_x
    else:
        parent[p_x] = p_y



for _ in range(M):
    x, y = map(int, input().split(' '))
    union(x, y)


candy_set = [[0,0] for _ in range(N+1)]


for i in range(1, N+1):
    candy_set[find(i)][1] += candy[i]
    candy_set[find(i)][0] += 1

candy_set.sort()

idx = 0
for i in range(len(candy_set)):
    if candy_set[i][0] != 0:
        idx = i
        break

candy_set = candy_set[idx:]

dp = [[0 for _ in range(K+1)] for _ in range(len(candy_set)+1)]

for i in range(1, len(candy_set)+1):
    for j in range(K):
        num, value = candy_set[i-1][0], candy_set[i-1][1]

        # 이번게 들어갈 공간이 난다면
        if 0 <= j - num:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-num] + value)
        else:
            dp[i][j] = dp[i-1][j]

print(max(dp[-1]))