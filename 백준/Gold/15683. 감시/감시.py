# 4^8 가지 경우의 수
# 2^16 가지 경우의 수 -> 64 & 1024, 64
import itertools

N, M = map(int, input().split(' '))
board = [list(map(int, input().split(' '))) for _ in range(N)]

CCTVS = []

for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            CCTVS.append([i, j, board[i][j]])

# 방향 0,1,2,3
# CCTV -> K개 일때 ( 8 )

K = len(CCTVS)
_type = [i for i in range(4)]
case = list(itertools.product(_type, repeat=K))
temp_board = [i[:] for i in board]


def camera(x, y, dx, dy, temp_board):
    cur_x, cur_y = x, y
    while True:
        if not (0 <= cur_x < N and 0<= cur_y <M):
            break
        if temp_board[cur_x][cur_y] == 6:
            break
        temp_board[cur_x][cur_y] = '#'
        cur_x += dx
        cur_y += dy

# case = [[0,1,2,3][1,2,3,4]..]

move = [[0,1],[1,0],[0,-1],[-1,0]]

answer = N * M
for directions in case:
    temp_board = [i[:] for i in board]
    for camera_id, direction in enumerate(directions):
        x, y, _type = CCTVS[camera_id][:]

        # type에 따라 입력값이 정해짐
        if _type == 1:
            _dir = direction % 4
            # direction 0
            dx, dy = move[_dir][:]
            camera(x, y, dx, dy, temp_board)
        elif _type == 2:
            # direction 0, 2
            _dir = direction % 4
            dx, dy = move[_dir][:]
            camera(x, y, dx, dy, temp_board)

            _dir = (direction + 2) % 4
            dx, dy = move[_dir][:]
            camera(x, y, dx, dy, temp_board)
        elif _type == 3:
            # direction 0, 3
            _dir = direction % 4
            dx, dy = move[_dir][:]
            camera(x, y, dx, dy, temp_board)

            _dir = (direction + 3) % 4
            dx, dy = move[_dir][:]
            camera(x, y, dx, dy, temp_board)

        elif _type == 4:
            # direction 0, 2, 3
            _dir = direction % 4
            dx, dy = move[_dir][:]
            camera(x, y, dx, dy, temp_board)

            _dir = (direction + 2) % 4
            dx, dy = move[_dir][:]
            camera(x, y, dx, dy, temp_board)

            _dir = (direction + 3) % 4
            dx, dy = move[_dir][:]
            camera(x, y, dx, dy, temp_board)

        elif _type == 5:
            # direciton 0, 1, 2, 3
            _dir = direction % 4
            dx, dy = move[_dir][:]
            camera(x, y, dx, dy, temp_board)

            _dir = (direction + 1) % 4
            dx, dy = move[_dir][:]
            camera(x, y, dx, dy, temp_board)

            _dir = (direction + 2) % 4
            dx, dy = move[_dir][:]
            camera(x, y, dx, dy, temp_board)

            _dir = (direction + 3) % 4
            dx, dy = move[_dir][:]
            camera(x, y, dx, dy, temp_board)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp_board[i][j] == '#' or temp_board[i][j] == 6:
                cnt += 1
    temp = N * M - cnt

    if answer > temp:
        answer = temp

print(answer)

