# dfs : n과m 다 풀고 14888 2580 1987
# bfs : 7562 7576 1697 13459
# dp : 2747 9095 11726 11051 1149 2156 9251 11049
# 다잌 : 1916 1504 12763  1854

# 1 -> a -> b -> N
# 1 -> b -> a -> N
import heapq
n = int(input())
T, M = map(int, input().split(' '))
L = int(input())


nodes = [[] for _ in range(n + 1)]
for i in range(L):
    a, b, time, cost = map(int, input().split(' '))
    nodes[a].append((b, time, cost))
    nodes[b].append((a, time, cost))

# 최소이긴한데, 최소일때가 아니라 T분이내일때의 값들을 저장...! 그것들 중 최소값!
def dijkstra(src, dst) -> int:
    """
    :param src(int):
    :param dst(int):
    :return score(int):
    """
    if src == dst:
        return 0

    total_cost = 1000000000
    queue = []
    heapq.heapify(queue)

    for next, time, cost in nodes[src]:
        if time <= T and cost <= M:
            heapq.heappush(queue, (time, cost, next))

    while queue:
        cur_time, cur_cost, cur_node = heapq.heappop(queue)

        if cur_node == dst:
            if total_cost > cur_cost:
                total_cost = cur_cost
                continue

        for next, time, cost in nodes[cur_node]:
            if cur_time + time <= T and cur_cost + cost <= M:
                heapq.heappush(queue, (cur_time+time, cur_cost + cost, next))

    if total_cost == 1000000000:
        return -1
    else:
        return total_cost


print(dijkstra(1,n))

