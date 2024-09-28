# 리스트[y][x]

# 0번
# 1번 -y, x
# 2번 -x, -y
# 3번 y, -x

# 시계 90 => y, -x

# 1세대 0,0 1,0 1,-1
# 2세대 0,0 1,0 1,-1 0,-1 0,-2
# 3세대 0,0 1,0 1,-1 0,-1 0,-2, -1, -2, -1, -1, -2, -1, -2, -2

N = int(input())
curve = [list(map(int, input().split(' ')))for _ in range(N)]
graph = [[False for _ in range(101)] for _ in range(101)]
move = [(1,0), (0,-1), (-1,0), (0,1)]

def next_gen(points):
    # 0,0 1,0 1,-1이 왔다치면
    sub = points[0:-1]
    last = points[-1]

    for i in range(len(sub)-1, -1, -1):
        x, y = sub[i][0] - last[0], sub[i][1] - last[1]
        
        # 회전
        points.append((-y + last[0], x + last[1]))

    return points


for x, y, d, g in curve:
    points = [(x, y), (x+move[d][0], y+move[d][1])]

    for i in range(g):
        points = next_gen(points)
    
    for p_x, p_y in points:
        graph[p_y][p_x] = True

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            answer += 1

print(answer)

