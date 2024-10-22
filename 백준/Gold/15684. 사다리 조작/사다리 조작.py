N, M, H = map(int, input().split(' '))
# 세로선, 가로선 총 개수, 위치 개수 H
# 가로선 개수 M

# 격자를 하나의 그것으로...

# N개
# H

# depth 1, 2, 3, 4 ..
# 1, 1, 2
# 2, 1, 2
# ...
# 2, 1, 2
# ...
line_base = [list(map(int, input().split(' '))) for _ in range(M)]
line_info = [[False for _ in range(N + 2)] for _ in range(H + 2)]

for x, y in line_base:
    line_info[x][y] = True


def move(i):
    start_x, start_y = 1, i

    while True:
        # print(start_x, start_y)
        if line_info[start_x][start_y]:
            start_y += 1
            start_x += 1
        elif line_info[start_x][start_y - 1]:
            start_y -= 1
            start_x += 1
        else:
            start_x += 1

        if start_x == H + 1:
            break
    if start_y == i:
        return True
    else:
        return False


min_cnt = [300]


def btk(cnt):
    if cnt >= min_cnt[0]:  # 최소값보다 크면 더 이상 탐색할 필요 없음
        return
    
    is_True = True
    for j in range(1, N + 1):
        flag = move(j)

        if not flag:
            is_True = False
            break

    if is_True:
        if cnt < min_cnt[0]:
            min_cnt[0] = cnt

    if cnt == 3:
        return

    for i in range(1, H + 1):
        for j in range(1, N):
            if line_info[i][j] or line_info[i][j - 1] or line_info[i][j + 1]:
                continue
            line_info[i][j] = True
            btk(cnt + 1)
            line_info[i][j] = False


btk(0)
if min_cnt[0] > 3:
    print(-1)
else:
    print(min_cnt[0])
