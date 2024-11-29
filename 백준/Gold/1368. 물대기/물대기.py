
n = int(input())

fountain_cost = [int(input()) for _ in range(n)]
graph = [list(map(int, input().split(' '))) for _ in range(n)]

parent = [i for i in range(n+1)]

edges = []

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(a, b):
    p_a, p_b = find(a), find(b)

    if p_a == p_b:
        return

    if p_a > p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b

    return


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        edges.append([i,j,graph[i][j]])

for i in range(n):
    edges.append([n,i,fountain_cost[i]])
edges.sort(key=lambda x: x[2])


answer = 0
candi = []
is_first = 0
for i, j, cost in edges:

    p_i, p_j = find(i), find(j)
    if p_i == p_j:
        continue

    union(i,j)
    answer += cost

print(answer)

# 0 1 2 3
# 2 -> 3 -> 1 -> 0