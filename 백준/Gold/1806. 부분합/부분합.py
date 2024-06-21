# 10000이하 자연수, 길이 N
# 연속된 수들의 합중 S 이상이 되는것 중 가장 짧은거...!

import sys
import bisect
input = sys.stdin.readline
N, S = map(int, input().split())
seq = list(map(int, input().split()))
answer = 100001
# 누적합 생성
for i in range(1, N):
    seq[i] += seq[i-1]

for i in range(N):
    if seq[i] < S:
        continue

    pos = bisect.bisect_right(seq, seq[i] - S)
    answer = min(answer, i - pos)

if answer == 100001:
    print(0)
else:
    print(answer+1)

