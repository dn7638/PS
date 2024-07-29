import sys

input = sys.stdin.readline
from collections import deque

N, R, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
queue = deque()
_queue = []

visited = [False] * (N+1)
visited[R] = True
queue.append(R)
parents = [0] * (N+1)
parents[R] = R

while queue:
    node = queue.popleft()
    _queue.append(node)
    for child in graph[node]:
        if not visited[child]:
            parents[child] = node   
            queue.append(child)
            visited[child] = True

accumlate = [1] * (N+1)

for i in range(len(_queue)-1, 0, -1):
    node = _queue[i]
    accumlate[parents[node]] += accumlate[node]

query = [int(input()) for _ in range(Q)]

for root in query:
    print(accumlate[root])


# 9
# 4
# 1