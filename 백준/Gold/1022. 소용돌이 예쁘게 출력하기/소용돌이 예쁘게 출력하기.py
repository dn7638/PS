r1, c1, r2, c2 = map(int, input().split(' '))

def de(num):
    cnt = 1
    while True:
        if num // 10 > 0:
            num //= 10
            cnt += 1
        else:
            return cnt

field = [[0 for _ in range(5)] for _ in range(50)]

move = [[0, 1], [-1, 0], [0, -1], [1, 0]]

cur_x, cur_y = 0, 0
field[0][0] = 1
if r1 <= cur_x <= r2 and c1 <= cur_y <= c2:
    field[cur_x - r1][cur_y - c1] = 1

cur_num = 1
max_num = 0
loop_out_flag = True

R = r2 - r1
C = c2 - c1
loop = 1

while True:
    for idx, d in enumerate(move):
        dx, dy = d[:]
        for _ in range(loop):
            cur_x, cur_y = cur_x + dx, cur_y + dy

            if not (-5001 <= cur_x <= 5001 and -5001 <= cur_y <= 5001):
                loop_out_flag = False
                break

            cur_num += 1
            if r1 <= cur_x <= r2 and c1 <= cur_y <= c2:
                field[cur_x - r1][cur_y - c1] = cur_num
                max_num = cur_num

        if not loop_out_flag:
            break

        if idx % 2 == 1:
            loop += 1
    if not loop_out_flag:
        break

num_10 = de(max_num)

for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(f'{field[i][j]:{num_10}d}', end=' ')
    print()


# 우 1 3
# 상 1 3
# 좌 2 4
# 하 2 4
