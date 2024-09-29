from collections import deque

N, M = map(int, input().split(' '))

board = [list(input().rstrip())for _ in range(N)]

B = (-1,-1)
R = (-1,-1)
dest = (-1,-1)
move = [[0,1], [0,-1], [1,0], [-1,0]]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            B = (i, j)
        elif board[i][j] == 'R':
            R = (i, j)
        elif board[i][j] == 'O':
            dest = (i, j)

queue = deque()

def move_ball(dx, dy, x, y):
    while True:
        if board[x+dx][y+dy] == '#':
            return (x, y)
        elif board[x+dx][y+dy] == 'O':
            x += dx
            y += dy
            return (x, y)
        else:
            x += dx
            y += dy

def get_distance(src, dest):
    srcx, srcy = src[0], src[1]
    destx, desty = dest[0], dest[1]
    return abs(srcx - destx) + abs(srcy - desty)
    

for x, y in move:
    queue.append((1, x, y, B, R))

answer = -1
while queue:
    cnt, dx, dy, cur_B, cur_R = queue.popleft()
    
    # 한쪽 방향으로 기울이기
    next_B = move_ball(dx, dy, cur_B[0], cur_B[1])
    next_R = move_ball(dx, dy, cur_R[0], cur_R[1])

    # 둘다 구멍에 빠졌는지 확인
    if next_R[0] == dest[0] and next_R[1] == dest[1]:
        if next_B[0] == dest[0] and next_B[1] == dest[1]:
            continue
            # False
        else:
            answer = cnt
            break
            # True tjdrhd
    else:
        if next_B[0] == dest[0] and next_B[1] == dest[1]:
            continue

    next_R_x = next_R[0]
    next_R_y = next_R[1]
    next_B_x = next_B[0]
    next_B_y = next_B[1]
    # print(next_R_x, next_R_y, next_B_x ,next_B_y)
    # 둘이 겹치면
    if next_B[0] == next_R[0] and next_B[1] == next_R[1]:
        dist_R = get_distance(cur_R, next_R)
        dist_B = get_distance(cur_B, next_B)
        
        
        # 더 멀리있는애가 그 전에 위치함
        if dist_R > dist_B:
            next_R_x = next_R[0] - dx
            next_R_y = next_R[1] - dy
        else:
            next_B_x = next_B[0] - dx
            next_B_y = next_B[1] - dy
    
    cnt += 1
    if cnt > 10:
        continue

    for _dx, _dy in move:
        queue.append((cnt, _dx, _dy, (next_B_x, next_B_y), (next_R_x, next_R_y)))

print(answer)


