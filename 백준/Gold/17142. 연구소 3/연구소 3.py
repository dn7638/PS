from collections import deque
import itertools

n, m = map(int, input().split(' '))
board = [list(map(int, input().split(' '))) for _ in range(n)]
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

b_list = []
should_find_cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            b_list.append((i, j))
        elif board[i][j] == 0:
            should_find_cnt += 1

b_cnt = len(b_list)
# 10C5 -> 10 9 8 7 6 // 5 4 3 2 1 = 3 2 7 6 = 42 6 = 252
b_combi = list(itertools.combinations(b_list, m))

# 252번 반복
answer = n ** 2
for i in b_combi:
    visited = [[False for _ in range(n)] for _ in range(n)]

    # 큐에 바이러스 좌표 삽입
    queue = deque()
    for j in i:
        x, y = j[0], j[1]
        queue.append((x, y, 0))
        visited[x][y] = True
    last_cnt = -1
    is_success = False
    total_find_cnt = 0
    while queue:
        cur_x, cur_y, cnt = queue.popleft()
        last_cnt = cnt
        if board[cur_x][cur_y] != 2:
            total_find_cnt += 1

        if should_find_cnt == total_find_cnt:
            is_success = True
            break

        for dx, dy in move:
            next_x, next_y = cur_x + dx, cur_y + dy
            if not (0 <= next_y < n and 0 <= next_x < n):
                continue
            if visited[next_x][next_y]:
                continue
            if board[next_x][next_y] == 1:
                continue

            queue.append((next_x, next_y, cnt+1))
            visited[next_x][next_y] = True

    if not (should_find_cnt == total_find_cnt):
        continue

    if last_cnt == -1:
        last_cnt = 0
    if answer > last_cnt:
        answer = last_cnt

if answer == n ** 2:
    print(-1)
else:
    print(answer)
