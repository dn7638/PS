from collections import deque

# i 보다 작은 면적을 구한다
# 단 그 면적이 맨 바깥이라면 성립하지 않는다

N, M = map(int, input().split(' '))
board = [list(map(int, list(input()))) for _ in range(N)]
move = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def innate(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    else:
        return False


def is_edge(x, y):
    if 0 < x < N - 1 and 0 < y < M - 1:
        return False
    else:
        return True


def i_floor(num):
    visited = [[False for _ in range(M)] for _ in range(N)]

    total = 0
    for i in range(N):
        for j in range(M):
            if not innate(i, j):
                continue
            if visited[i][j]:
                continue
            if board[i][j] >= num:
                continue

            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            cnt = 1
            edge_flag = False
            while queue:
                cur_x, cur_y = queue.popleft()

                if is_edge(cur_x, cur_y):
                    edge_flag = True

                for dx, dy in move:
                    next_x, next_y = cur_x + dx, cur_y + dy
                    if not innate(next_x, next_y):
                        continue
                    if visited[next_x][next_y]:
                        continue
                    if board[next_x][next_y] >= num:
                        continue
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True
                    cnt += 1
            if edge_flag:
                cnt = 0
            total += cnt

    return total


answer = 0
for i in range(2, 10):
    temp = i_floor(i)
    answer += temp

print(answer)
