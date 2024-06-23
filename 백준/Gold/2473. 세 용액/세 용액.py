# 시간복잡도 분석
# 3가지 용액
# 전체 용액 수 -> 5000
# 5000C3 = 5000^3 125000000000 1000억...!
# 5000 * ln5000 가능
# 정렬 -> 투포인터 사용가능
# 해당 상황에서 완탐 -> 5000 * 5000 vs bis search -> 5000 * ln5000

# 상황 파악
# -12 -5 -3 1 2 5 19
# case 1 : -12 + 19 + x
# 7 + x
# -7 가 어디로 가야할까요?
# 0 idx로 가야햠..!
# 이때 left보다 같거나 작으면 left + 1
# left 보다 크면 그거

# -12 -5 -3 1 2 5 7
# case 1 : -12 + 7 + x
# -5 + x
# 5가 어디로 가야 할까요?

# 사고 과정
# 아무튼 이진탐색 결과 idx와 idx+1의 값을 비교하여 더 가까운 것을 찾아야함
# 가장 가까운 결과를 update...!
# 이때 현재 left, right 에 따라서 결과 조정해아함...!!

import sys
import bisect

input = sys.stdin.readline
N = int(input())
seq = list(map(int, input().split()))
seq.sort()


answer = 3000000000
answer_list = [0, 0, 0]

for i in range(N - 2):
    C = seq[i]
    left, right = i+1, N - 1
    while left < right:
        A, B = seq[left], seq[right]

        if A + B + C > 0:
            right -= 1
        elif A + B + C < 0:
            left += 1
        else:
            answer_list[0], answer_list[1], answer_list[2] = C, A, B
            break

        if abs(A + B + C) < answer:
            answer = abs(A + B + C)
            answer_list[0], answer_list[1], answer_list[2] = C, A, B
    if answer == 0:
        break

print(f'{answer_list[0]} {answer_list[1]} {answer_list[2]}')

# -5 -3 2 1
# -100  1 2 3
