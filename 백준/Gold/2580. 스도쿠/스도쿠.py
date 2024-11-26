board = [list(map(int, input().split(' '))) for _ in range(9)]

loc_zero = []
answer = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            loc_zero.append((i, j))

num_zero = len(loc_zero)


def check(i, j, num):
    for k in range(9):
        if board[i][k] == num:
            return False

    for k in range(9):
        if board[k][j] == num:
            return False

    _i = (i // 3) * 3
    _j = (j // 3) * 3
    for k in range(3):
        for l in range(3):
            if board[_i + k][_j + l] == num:
                return False

    return True


def btk(num_zero, cnt):
    # pruning
    if cnt == num_zero:
        answer = [x[:] for x in board]
        for i in answer:
            print(' '.join(map(str, i)))
        exit()
        # 종료 조건

    for i in range(1, 10):
        x, y = loc_zero[cnt][:]

        flag = check(x, y, i)

        if flag:
            board[x][y] = i
            btk(num_zero, cnt + 1)
            board[x][y] = 0


btk(num_zero, 0)

# 1 3 4 4 9 5 7 2 7 3 4 4 8 1

