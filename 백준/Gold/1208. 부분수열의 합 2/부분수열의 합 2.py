import sys
from collections import deque
import bisect

input = sys.stdin.readline
# N 개 정수

N, S = map(int, input().split(' '))
# 합이 S

seq = list(map(int, input().split(' ')))
left = seq[:N // 2]
right = seq[N // 2:]

left_sum = []
right_sum = []

queue = deque()
queue.append((0, 0))

# 0000000000
# 0000000001
# 0000000010
# 0000.....
# 1111111111
while queue:
    cur_sum, cur_cnt = queue.popleft()
    if cur_cnt == N // 2:
        left_sum.append(cur_sum)
        continue

    queue.append((cur_sum, cur_cnt + 1))
    queue.append((cur_sum + left[cur_cnt], cur_cnt + 1))

queue = deque()
queue.append((0, 0))

while queue:
    cur_sum, cur_cnt = queue.popleft()
    if cur_cnt == len(right):
        right_sum.append(cur_sum)
        continue

    queue.append((cur_sum, cur_cnt + 1))
    queue.append((cur_sum + right[cur_cnt], cur_cnt + 1))

answer = 0
left_sum.sort()
right_sum.sort()
for i in range(len(left_sum)):
    answer += (bisect.bisect_right(right_sum, S - left_sum[i]) - bisect.bisect_left(right_sum, S - left_sum[i]))


if S == 0:
    answer -= 1
print(answer)
