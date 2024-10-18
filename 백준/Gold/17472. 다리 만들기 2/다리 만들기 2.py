from collections import deque

N, M = map(int, input().split(' '))
board = [list(map(int, input().split(' '))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

def row_check(row_num):
    result = []
    start_node = 0
    cnt = 0
    for j in range(M):
        if board[row_num][j] == 0:
            cnt += 1
            continue

        if start_node == 0:
            start_node = board[row_num][j]
            cnt = 0
        else:
            end_node = board[row_num][j]
            if cnt >= 2:
                result.append((cnt, start_node, end_node))
            cnt = 0
            start_node = end_node
    return result


def col_check(col_num):
    result = []
    start_node = 0
    cnt = 0
    for j in range(N):
        if board[j][col_num] == 0:
            cnt += 1
            continue

        if start_node == 0:
            start_node = board[j][col_num]
            cnt = 0
        else:
            end_node = board[j][col_num]
            if cnt >= 2:
                result.append((cnt, start_node, end_node))
            cnt = 0
            start_node = end_node
    return result


# 1 - 3 - 5
def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a == parent_b:
        return

    # 작은게 루트가 되게 하자..!
    if parent_a > parent_b:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a

    return


def innate(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    else:
        return False


move = [[0, 1], [1, 0], [-1, 0], [0, -1]]
queue = deque()
num = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue

        if board[i][j] == 0:
            continue

        num += 1

        queue.append((i, j))
        visited[i][j] = True

        while queue:
            cur_x, cur_y = queue.popleft()
            board[cur_x][cur_y] = num
            for dx, dy in move:
                next_x, next_y = cur_x + dx, cur_y + dy
                if not innate(next_x, next_y):
                    continue
                if board[next_x][next_y] == 0:
                    continue
                if visited[next_x][next_y]:
                    continue
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True


edges = []
parent = [i for i in range(num+1)]

for i in range(N):
    edges.extend(row_check(i))

for i in range(M):
    edges.extend(col_check(i))

edges.sort()


answer = 0
for length, node_src, node_dst in edges:
    parent_src = find(node_src)
    parent_dst = find(node_dst)

    # 같은 집합인지 확인
    if parent_src == parent_dst:
        # 같은 집합이면 pass
        continue

    # 다른 집합이면 간선 연결 후 union
    union(node_src, node_dst)
    answer += length

is_connected = True
for i in range(1, num):
    if find(i) != find(i+1):
        is_connected = False
        break

if answer == 0 or not is_connected:
    print(-1)
else:
    print(answer)



