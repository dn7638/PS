from collections import deque
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split(' '))
A = [list(map(int, input().split(' '))) for _ in range(N)]
trees = [list(map(int, input().split(' '))) for _ in range(M)]
space = [[5 for _ in range(N+1)] for _ in range(N+1)]

# (-1, -1), (-1, 0), (-1, 1)
# (0, -1), (0, 0), (0, 1)
# (1, -1), (1, 0), (1, 1)
move = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
trees.sort(key=lambda x: x[2])
queue = deque(trees)
for i in range(K):

    # 봄
    
    temp = deque()
    dead = []
    big = []

    while queue:
        x, y, z = queue.popleft()
        if space[x][y] >= z:
            space[x][y] -= z
            z += 1
            temp.append((x, y, z))
            if z % 5 == 0:
                big.append((x,y,z))
        else:
            dead.append((x, y, z))

    # for x, y, z in trees:
    #     if space[x][y] >= z:
    #         space[x][y] -= z
    #         z += 1
    #         temp.append((x, y, z))
    #         if z % 5 == 0:
    #             big.append((x,y,z))
    #     else:
    #         # dead.append((x, y, z))
    #         space[x][y] += (z//2)
    queue = temp

    # 여름    
    for x, y, z in dead:
        space[x][y] += (z//2)


    # 가을
    temp = []
    for x, y, z in big:
        if z % 5 == 0:
            for dx, dy in move:
                if 1<= x+dx <= N and 1<= y+dy <= N:
                    queue.appendleft((x+dx, y+dy, 1))
                    # temp.append((x+dx, y+dy, 1))
    
    # trees.extend(temp)

    # 겨울
    for i in range(1, N+1):
        for j in range(1, N+1):
            space[i][j] += A[i-1][j-1]

print(len(queue))



