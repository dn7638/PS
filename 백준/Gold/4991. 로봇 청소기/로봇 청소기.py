from collections import deque

move = [[-1, 0], [1, 0], [0, 1], [0, -1]]

def cal_cur_next(cur_x, cur_y, next_x, next_y):
    h, w = len(board), len(board[0])
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque()
    queue.append((cur_x, cur_y, 0))
    visited[cur_x][cur_y] = True
    while queue:
        c_x, c_y, cnt = queue.popleft()

        if c_x == next_x and c_y == next_y:
            return cnt

        for dx, dy in move:
            n_x, n_y = c_x + dx, c_y + dy
            if not (0 <= n_x < h and 0 <= n_y < w):
                continue
            if visited[n_x][n_y]:
                continue
            if board[n_x][n_y] == 'x':
                continue
            visited[n_x][n_y] = True
            queue.append((n_x, n_y, cnt + 1))
    return -1


def btk(dir_len, x, y, total_move):
    move_result = 0
    if len(dir_seq) > 0:
        if 1 == len(dir_seq):
            src = dir_seq[-1]
        else:
            src = dir_seq[-2]

        dst = dir_seq[-1]
        move_result = distance[src][dst]

        if move_result == -1:
            return

    total_move += move_result
    if len(dir_seq) == dir_len:  # 더러운방 숫자
        if answer[0] > total_move:
            answer[0] = total_move
        return
    else:
        if answer[0] <= total_move:
            return

    for idx in range(dir_len):
        if idx in dir_seq:
            continue
        dir_seq.append(idx)
        btk(dir_len, x, y, total_move)
        dir_seq.pop()


while True:
    w, h = map(int, input().split(' '))

    if w == 0 and h == 0:
        break

    board = [list(input().rstrip()) for _ in range(h)]
    dir_list = []
    start_x, start_y = -1, -1

    # 더러운칸 10개 이하
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                dir_list.append((i, j))
            elif board[i][j] == 'o':
                start_x, start_y = i, j

    distance = [[0 for _ in range(len(dir_list))] for _ in range(len(dir_list))]

    for i in range(len(distance)):
        for j in range(i, len(distance)):
            if i == j:
                src_x, src_y = start_x, start_y
                dst_x, dst_y = dir_list[j]
                distance[i][i] = cal_cur_next(src_x, src_y, dst_x, dst_y)
            else:
                src_x, src_y = dir_list[i]
                dst_x, dst_y = dir_list[j]
                temp = cal_cur_next(src_x, src_y, dst_x, dst_y)
                distance[i][j] = temp
                distance[j][i] = temp



    dir_seq = []
    answer = [w*h]
    btk(len(dir_list), start_x, start_y, 0)
    if answer[0] == w*h:
        print(-1)
    else:
        print(answer[0])
