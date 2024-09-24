from collections import deque   

N = int(input())
space = [list(map(int, input().split(' '))) for _ in range(N)]
shark_size = 2
eat_cnt = 0


def print_space(space):
    for i in space:
        print(i)


def find_shark_loacion(space):
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                space[i][j] = 0
                return (i, j)

shark_location = find_shark_loacion(space)

def is_eatable(space, shark_size):
    eatable_list = []
    for i in range(N):
        for j in range(N):
            if space[i][j] < shark_size and space[i][j] > 0:
                eatable_list.append((i,j))
    if not eatable_list:
        return False
    else:
        eatable_list.sort()
        x, y = eatable_list[0]
        return x, y


def is_innate(x, y):
    if 0<= x < N and 0<= y <N:
        return True
    else:
        return False
    
# 상 좌 하 우
move = [[-1, 0], [0, -1], [0, 1], [1, 0]]

answer = 0
while True:

    if not is_eatable(space, shark_size):
        break

    visited = [[False for _ in range(N)] for _ in range(N)]

    queue = deque()
    x, y = shark_location
    queue.append((x, y, 0))
    candidate = []

    while queue:
        cur_x, cur_y, move_cnt = queue.popleft()
        visited[cur_x][cur_y] = True
        if space[cur_x][cur_y] > 0 and space[cur_x][cur_y] < shark_size:
            candidate.append((move_cnt, cur_x, cur_y))
            if len(candidate) > 1:
                if candidate[-1][0] < move_cnt:
                    break
            

        for dx, dy in move:
            next_x, next_y = cur_x + dx, cur_y + dy
            if is_innate(next_x, next_y) and not visited[next_x][next_y] and space[next_x][next_y] <= shark_size:
                queue.append((next_x, next_y, move_cnt+1))
                visited[next_x][next_y] = True

    if candidate:
        candidate.sort()
        move_cnt, cur_x, cur_y =  candidate[0][0], candidate[0][1], candidate[0][2]
        space[cur_x][cur_y] = 0
        eat_cnt += 1
        answer += move_cnt
        shark_location = cur_x, cur_y
        if eat_cnt == shark_size:
            shark_size += 1
            eat_cnt = 0
    else:
        break
print(answer)
