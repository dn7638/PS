import heapq
from collections import deque

n, m, k = map(int, input().split(' '))
nodes = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, time = map(int, input().split(' '))
    nodes[a].append((time, b))

pass_list = [[] for _ in range(n+1)]
# 방문 가능? 불가능?

# 방문 불가능이더라도 -> 1번째면?
def dijkstra(k):

    queue = []
    heapq.heappush(queue, (0, 1))
    heapq.heappush(pass_list[1],[0,0])

    while queue:

        cur_time, cur_node = heapq.heappop(queue)

        for time, next in nodes[cur_node]:
            if len(pass_list[next]) < k:
                heapq.heappush(queue, (cur_time + time, next))
                heapq.heappush(pass_list[next], [-(cur_time + time), cur_time + time])
            elif pass_list[next][0][1] > cur_time + time:
                heapq.heappush(queue, (cur_time+time, next))
                heapq.heappop(pass_list[next])
                heapq.heappush(pass_list[next], [-(cur_time+time), cur_time+time])


dijkstra(k)

# for i in pass_list:
#     print(i)

for i in range(1,n+1):
    if len(pass_list[i]) < k:
        print(-1)
    else:
        print(pass_list[i][0][1])
