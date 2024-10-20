from collections import deque

dst_int = int(input().rstrip())
M = int(input().rstrip())
dst_str = list(map(int, list(str(dst_int))))

result = 500000
if M > 0:
    buttons = set(list(map(int, input().split(' '))))
    stack = deque()
    stack.append((0,0))

    while stack:
        num, cnt = stack.pop()


        if cnt == 0:
            number = 100
        else:
            number = num

        # |만들어진 숫자 - 목표| + 숫자를 누른 횟수
        temp = min(abs(dst_int - number) + cnt, abs(dst_int - 100))

        if result > temp:
            result = temp

        if cnt == len(dst_str) + 1:
            continue

        for i in range(10):
            if i in buttons:
                continue
            stack.append((num * 10 + i, cnt + 1))

    print(result)

else:
    print(min(abs(dst_int-100), len(str(dst_int))))
