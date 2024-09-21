
_max = 100000 * 4

# 100000 * 4 * 4
dp = [[[ _max for _ in range(5)] for _ in range(5)] for _ in range(100001)]
dp[0][0][0] = 0

seq = list(map(int, input().split(' ')))

def get_value(src, dest):
    if src == 0:
        return 2
    value = abs(src - dest)
    if value == 0:
        return 1
    elif value == 1 or value == 3:
        return 3
    elif value == 2:
        return 4


for i in range(len(seq)-1):
    next = seq[i]
    if i == 0:
        dp[0][0][next] = get_value(0, next)
        # dp[0][next][0] = get_value(0, next)
        dp[0][0][0] = _max
        continue

    for j in range(5):
        for k in range(5):
            x, y = j, k
            if x == y :
                continue

            if dp[i-1][x][y] >= _max:
                continue
            else:
                if x == next:
                    dp[i][next][y] = min(dp[i][next][y], dp[i-1][x][y] + get_value(x, next))
                elif y == next:
                    dp[i][x][next] = min(dp[i][x][next], dp[i-1][x][y] + get_value(y, next))
                else:
                    dp[i][x][next] = min(dp[i][x][next], dp[i-1][x][y] + get_value(y, next))
                    dp[i][next][y] = min(dp[i][next][y], dp[i-1][x][y] + get_value(x, next))

                

result = _max

for val in dp[len(seq)-2]:
    result = min(result, min(val))


print(result)
