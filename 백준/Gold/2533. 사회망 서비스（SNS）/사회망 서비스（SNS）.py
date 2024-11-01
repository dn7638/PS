from collections import deque
import sys

inpu = sys.stdin.readline
# 리프노드의 개수를 구하기

N = int(input())
edges = [list(map(int, input().split(' '))) for _ in range(N-1)]
nodes = [[] for _ in range(N+1)]
early = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]

# dp[i][0], dp[i][1] i번 노드가 얼리어댑터인경우 1, 아닌경우 0
dp = [[0,1] for _ in range(N+1)]

for x, y in edges:
    nodes[x].append(y)
    nodes[y].append(x)


depth_list = []
depth_list_set = []

def bfs():
    queue = deque()
    queue.append((1, 0))
    visited[1] = True


    while queue:
        node, depth = queue.popleft()

        # 1
        if len(depth_list) == depth:
            depth_list.append([])
            depth_list_set.append(set())

        depth_list[depth].append(node)
        depth_list_set[depth].add(node)

        for next_node in nodes[node]:
            if visited[next_node]:
                continue
            visited[next_node] = True
            queue.append((next_node, depth+1))

bfs()


# 깊이의 역순으로 탐색할 예정
for depth in range(len(depth_list) - 2, -1, -1):
    for node in depth_list[depth]:

        # 리프이면 False, 넘어감
        # if len(nodes[node]) == 1:
        #     continue

        is_all_True = True

        for child in nodes[node]:
            if depth > 0:
                if child in depth_list_set[depth-1]:
                    continue
            # 내가 얼리어댑터가 아님
            dp[node][0] += dp[child][1]

            # 내가 얼리어댑 임
            dp[node][1] += min(dp[child][0], dp[child][1])




print(min(dp[1]))

# 1 : 2
# 2 : 1, 3
# 3 : 2