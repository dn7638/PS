# dfs : n과m 다 풀고 14888 2580 1987
# bfs : 7562 7576 1697 13459
# dp : 2747 9095 11726 11051 1149 2156 9251 11049
# 다잌 : 1916 1504 12763  1854

# 1 -> a -> b -> N
# 1 -> b -> a -> N
import heapq

n, e = map(int, input().split(' '))

nodes = [[] for _ in range(n + 1)]
for i in range(e):
    a, b, cost = map(int, input().split(' '))
    nodes[a].append((b, cost))
    nodes[b].append((a, cost))
a, b = map(int, input().split(' '))


def dijkstra(src, dst) -> int:
    """
    :param src(int):
    :param dst(int):
    :return score(int):
    """
    if src == dst:
        return 0
    cost_list = [2100000000 for _ in range(n + 1)]
    queue = []
    heapq.heapify(queue)

    for next, cost in nodes[src]:
        heapq.heappush(queue, (cost, next))

    while queue:
        cur_cost, cur_node = heapq.heappop(queue)

        if cur_node == dst:
            return cur_cost

        if cost_list[cur_node] > cur_cost:
            cost_list[cur_node] = cur_cost
        else:
            continue

        for next, cost in nodes[cur_node]:
            heapq.heappush(queue, (cur_cost + cost, next))
    return -1

# 1 -> a -> b -> N
# 1 -> b -> a -> N
a1 = dijkstra(1, a)
a2 = dijkstra(a, b)
a3 = dijkstra(b, n)

b1 = dijkstra(1, b)
b2 = dijkstra(b, a)
b3 = dijkstra(a, n)

if a1 == -1 or a2 == -1 or a3 == -1 or b1 == -1 or b2 == -1 or b3 == -1:
    print(-1)
else:
    print(min(a1 + a2 + a3,b1 + b2 + b3))
