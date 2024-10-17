R, C, M = map(int, input().split(' '))

# r, c, s, d, z
# 위치 : r,c | 속력 : s | 방향 : d | 크기 : z
shark_info = [list(map(int, input().split(' '))) for _ in range(M)]
shark_location = [[-1 for _ in range(C + 1)] for _ in range(R + 1)]

for idx, info in enumerate(shark_info):
    r, c, s, d, z = info[:]
    shark_location[r][c] = idx

direction = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1]]

# O(1000,000)
def catch_shark(i):
    for j in range(1, R + 1):
        idx = shark_location[j][i]
        if idx < 0:
            continue

        shark_info[idx][0], shark_info[idx][1] = -1,-1
        shark_location[j][i] = -1

        return shark_info[idx][4]

    return 0

def prt(a):
    for i in a:
        for j in i:
            if j == -1:
                print(0, end=' ')

            else:
                print(chr(j + ord('A')), end=' ')
        print()
    print('-----------')

def move_shark():
    for idx, info in enumerate(shark_info):
        # 위치 : r,c | 속력 : s | 방향 : d | 크기 : z
        # 0 ≤ s ≤ 1000
        r, c, s, d, z = info[:]
        dr, dc = direction[d][:]

        # 죽은 상어
        if r == -1 and c == -1:
            continue

        # 상어 이동
        # 경계를 넘어가면 방향을 반대로 바꿔서 속력 유치한 채로 이동
        n_r, n_c = r, c
        while s > 0:

            s -= 1
            n_r, n_c = n_r + dr, n_c + dc
            if not (1 <= n_r <= R and 1 <= n_c <= C):
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 4
                elif d == 4:
                    d = 3
                dr, dc = direction[d][:]
                n_r, n_c = n_r + 2 * dr, n_c + 2 * dc
        shark_info[idx][3] = d
        shark_info[idx][0], shark_info[idx][1] = n_r, n_c

    for i in range(R+1):
        for j in range(C+1):
            shark_location[i][j] = -1
        # 이동한 자리에 다른 상어 있는지 확인
        # idx 현재 상어 인덱스 | next_r, next_c
    for idx, info in enumerate(shark_info):
        # 위치 : r,c | 속력 : s | 방향 : d | 크기 : z
        # 0 ≤ s ≤ 1000
        r, c, s, d, z = info[:]

        # 죽은 상어
        if r == -1 and c == -1:
            continue

        other_shark_idx = shark_location[r][c]
        # big_idx = -1
        # small_idx = -1
        if other_shark_idx > -1:
            # 있으면 크기에 따라서 상어 먹기
            # 위치 : r,c | 속력 : s | 방향 : d | 크기 : z
            _r, _c, _s, _d, _z = shark_info[other_shark_idx][:]

            # 기존것이 더 큼
            if z < _z:
                big_idx = other_shark_idx
                small_idx = idx
            else:
                big_idx = idx
                small_idx = other_shark_idx

            shark_location[r][c] = big_idx
            shark_info[small_idx][0], shark_info[small_idx][1] = -1, -1
        else:
            shark_location[r][c] = idx

# prt(shark_location)

answer = 0
for i in range(1, C + 1):
    # 상어 잡기
    temp = catch_shark(i)
    answer += temp

    # 상어 이동
    move_shark()
    # prt(shark_location)

print(answer)

