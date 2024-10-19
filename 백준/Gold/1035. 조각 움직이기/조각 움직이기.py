import itertools
from collections import deque

board = [list(input().rstrip()) for _ in range(5)]

piece_cnt = 0
pieces = []
for i in range(5):
    for j in range(5):
        if board[i][j] == '*':
            piece_cnt += 1
            pieces.append([i, j])

if piece_cnt <= 1:
    print(0)
    exit()
location_list = [i for i in range(25)]

nCr = list(itertools.combinations(location_list, piece_cnt))


def length(src_r, src_c, dst_r, dst_c):
    return abs(src_r - dst_r) + abs(src_c - dst_c)


def btk(piece_cnt, temp, item, answer):
    if len(temp) == piece_cnt:
        total_len = 0

        for i in range(piece_cnt):
            r = item[temp[i]] // 5
            c = item[temp[i]] % 5
            _r, _c = pieces[i][:]
            t_length = length(r, c, _r, _c)
            total_len += t_length



        if answer[0] > total_len:
            answer[0] = total_len
            

        # 종료 조건
        return

    for i in range(piece_cnt):
        if i not in temp:
            temp.append(i)
            btk(piece_cnt, temp, item, answer)
            temp.pop()

answer = [100]
move = [[0,1],[0,-1],[1,0],[-1,0]]

for item in nCr:
    is_connected = True

    # item 5 * 5에 박고
    # bfs돌림 첫노드기준 방문가능 노드 개수 가지고 판단
    # 반문하면 cnt
    visited = [[False for _ in range(5)] for _ in range(5)]

    queue = deque()
    a, b = item[0] // 5, item[0] % 5
    queue.append((a, b))
    visited[a][b] = True

    cnt = 1
    while queue:
        cur_a, cur_b = queue.popleft()
        for dx, dy in move:
            next_a, next_b = cur_a+dx, cur_b+dy
            if not (0<= next_a < 5 and 0<= next_b < 5):
                continue
            if visited[next_a][next_b]:
                continue

            is_in = False
            for l in item:
                t_x, t_y = l // 5, l % 5
                if t_x == next_a and t_y == next_b:
                    is_in = True
                    break
            if not is_in:
                continue

            queue.append((next_a, next_b))
            visited[next_a][next_b] = True
            cnt += 1

    # 연결가능성 있는 item 세트
    if cnt == piece_cnt:
        temp = []
        btk(piece_cnt, temp, item, answer)

print(answer[0])


