# lis 문제 정벅...!

# 기본문제
# 길이만 출력하며댐
# 수열 크기 100만 -> N^2 안됨
# N log n 해야함
# A_i 크기는 100만이므로 100만 배열로 추적해도되고
# 추적 배열 만들어서 해결해도댐 (1, 값), (2, 값) ....
# 하지만 길이만 구하면 됨...!

import sys
import bisect

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

lis = []

lis.append(seq[0])
for i in range(1,N):

    pos = bisect.bisect_left(lis, seq[i])

    # 0 1 2
    # len(seq) = 3
    # if pos >= len(lis): 삽입
    # elif pos < len(lis) : 내부 교체

    if pos >= len(lis):
        lis.append(seq[i])
    elif pos < len(lis):
        lis[pos] = seq[i]

print(len(lis))

