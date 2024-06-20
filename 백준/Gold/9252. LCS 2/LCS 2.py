import sys

input = sys.stdin.readline
# ACAYKP
# CAPCAK
# 010010
# 1
# 122233

A = list(input().rstrip())
B = list(input().rstrip())

dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
for i in range(len(A)+1):
    for j in range(len(B)+1):

        if i == 0 or j == 0:
            continue
        elif A[i-1] == B[j-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # dp[i][j] 는 A의 i번째 원소까지의 단어 B의 j번째 까지의 단어

cnt = dp[len(A)][len(B)]
print(cnt)
flag = True
if cnt == 0:
    flag = False
answer = []

i = len(A)
j = len(B)
while cnt > 0:

    if dp[i - 1][j] == cnt:
        i -= 1
    elif dp[i][j - 1] == cnt:
        j -= 1
    else:
        answer.append(A[i-1])
        cnt -= 1
        i -= 1
        j -= 1

answer.reverse()

if answer:
    print(''.join(answer))
