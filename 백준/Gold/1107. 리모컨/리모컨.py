from collections import deque

dst_int = int(input().rstrip())
M = int(input().rstrip())
dst_str = list(map(int, list(str(dst_int))))

result = 500000
if M > 0:
    buttons = set(list(map(int, input().split(' '))))
    stack = deque()
    stack.append([])

    while stack:
        cur_list = stack.pop()

        if len(cur_list) == 0:
            number = 100
        else:
            number = int(''.join(list(map(str, cur_list))))

        # |만들어진 숫자 - 목표| + 숫자를 누른 횟수
        temp = min(abs(dst_int - number) + len(cur_list), abs(dst_int - 100))

        if result > temp:
            result = temp

        if len(cur_list) == len(dst_str) + 1:
            continue

        for i in range(10):
            if i in buttons:
                continue
            next_list = cur_list[:]
            next_list.append(i)
            stack.append(next_list)

    print(result)

else:
    print(min(abs(dst_int-100), len(str(dst_int))))
