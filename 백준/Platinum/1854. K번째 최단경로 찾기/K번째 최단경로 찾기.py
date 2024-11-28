import heapq

n, m, k = map(int, input().split(' '))
nodes = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, time = map(int, input().split(' '))
    nodes[a].append((time, b))

pass_list = [[] for _ in range(n + 1)]


def dijkstra(k):
    queue = []
    heapq.heappush(queue, (0, 1))
    heapq.heappush(pass_list[1], [0, 0])

    while queue:

        cur_time, cur_node = heapq.heappop(queue)

        for time, next in nodes[cur_node]:
            if len(pass_list[next]) < k:
                heapq.heappush(queue, (cur_time + time, next))
                heapq.heappush(pass_list[next], [-(cur_time + time), cur_time + time])

            # 노드, 간선 정보에 따라 항상 pass_list[next]에 최소 순서로 들어간다는 보장이 없음...! 그래서 힙사용
            elif pass_list[next][0][1] > cur_time + time:
                heapq.heappush(queue, (cur_time + time, next))
                heapq.heappop(pass_list[next])
                heapq.heappush(pass_list[next], [-(cur_time + time), cur_time + time])


dijkstra(k)

for i in range(1, n + 1):
    if len(pass_list[i]) < k:
        print(-1)
    else:
        print(pass_list[i][0][1])
