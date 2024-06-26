import sys

# puzzle = [[0 for _ in range(9)] for _ in range(9)]
puzzle = [ list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(9)]
# 012345678
# 9 10 ... 17
# 18

answer = False
def btk(cnt, num):
    global answer
    if answer:
        return

    x, y = cnt // 9, cnt % 9

    for i in range(9):
        if i == y:
            continue
        if puzzle[x][i] == num:
            return

    for i in range(9):
        if i == x:
            continue
        if puzzle[i][y] == num:
            return

    for i in range(3):
        if (x // 3)*3 + i == x:
            continue
        for j in range(3):
            if (y // 3) * 3 + j == y:
                continue

            if puzzle[(x // 3)*3 + i][(y // 3) * 3 + j] == num:
                return

    puzzle[x][y] = num

    if cnt == 80:
        answer = True
        for i in puzzle:
            for j in i:
                print(j, end='')
            print()
        return

    for i in range(1,10):
        _x, _y = (cnt + 1) // 9, (cnt + 1) % 9
        if _x > 8 or _y > 8:
            continue
        if puzzle[_x][_y] == 0:
            btk(cnt + 1, i)
            puzzle[_x][_y] = 0
        else:
            if puzzle[_x][_y] == i:
                btk(cnt + 1, i)
                puzzle[_x][_y] = i

for i in range(1,10):
    if puzzle[0][0] == 0:
        btk(0, i)
        puzzle[0][0] = 0
    else:
        if puzzle[0][0] == i:
            btk(0, i)
            puzzle[0][0] = i

