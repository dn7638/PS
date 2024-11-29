n = int(input())

parent = [i for i in range(n)]


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(a, b):
    parent_a, parent_b = find(a), find(b)

    if parent_a == parent_b:
        return

    # 작, 큰
    if parent_a > parent_b:
        parent[parent_b] = parent_a
        parent[parent_a] = parent_a
    else:
        parent[parent_a] = parent_b
        parent[parent_b] = parent_b
    return


x_idx = []
y_idx = []
z_idx = []

for i in range(n):
    x, y, z = map(int, input().split(' '))
    x_idx.append((x, i))
    y_idx.append((y, i))
    z_idx.append((z, i))

x_idx.sort()
y_idx.sort()
z_idx.sort()

edges = []

##
i, j = x_idx[0][1], x_idx[1][1]
distance = abs(x_idx[0][0] - x_idx[1][0])
edges.append([i, j, distance])

i, j = y_idx[0][1], y_idx[1][1]
distance = abs(y_idx[0][0] - y_idx[1][0])
edges.append([i, j, distance])

i, j = z_idx[0][1], z_idx[1][1]
distance = abs(z_idx[0][0] - z_idx[1][0])
edges.append([i, j, distance])
##
##
i, j = x_idx[n - 2][1], x_idx[n - 1][1]
distance = abs(x_idx[n - 2][0] - x_idx[n - 1][0])
edges.append([i, j, distance])

i, j = y_idx[n - 2][1], y_idx[n - 1][1]
distance = abs(y_idx[n - 2][0] - y_idx[n - 1][0])
edges.append([i, j, distance])

i, j = z_idx[n - 2][1], z_idx[n - 1][1]
distance = abs(z_idx[n - 2][0] - z_idx[n - 1][0])
edges.append([i, j, distance])

for i in range(1, n - 1):
    edges.append([x_idx[i][1], x_idx[i + 1][1], abs(x_idx[i][0] - x_idx[i + 1][0])])
    edges.append([x_idx[i][1], x_idx[i - 1][1], abs(x_idx[i][0] - x_idx[i - 1][0])])
    edges.append([y_idx[i][1], y_idx[i + 1][1], abs(y_idx[i][0] - y_idx[i + 1][0])])
    edges.append([y_idx[i][1], y_idx[i - 1][1], abs(y_idx[i][0] - y_idx[i - 1][0])])
    edges.append([z_idx[i][1], z_idx[i + 1][1], abs(z_idx[i][0] - z_idx[i + 1][0])])
    edges.append([z_idx[i][1], z_idx[i - 1][1], abs(z_idx[i][0] - z_idx[i - 1][0])])

edges.sort(key=lambda _x: _x[2])
answer = 0

for i, j, dis in edges:
    p_i, p_j = find(i), find(j)
    if p_i != p_j:
        union(i, j)
        answer += dis

print(answer)


