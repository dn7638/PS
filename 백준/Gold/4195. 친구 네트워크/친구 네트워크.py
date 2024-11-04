import sys

tc = int(input())

def find(x):
    parent_x = parent[x]
    if x == parent_x:
        return x
    else:
        parent[x] = find(parent_x)
        return parent[x]


def union(a, b):
    p_a, p_b = find(a), find(b)
    if p_a == p_b:
        return 
    parent[p_b] = p_a
    parent_cnt[p_a] = parent_cnt[p_a] + parent_cnt[p_b]


for _ in range(tc):
    f = int(sys.stdin.readline())
    parent = {}
    parent_cnt = {}
    for _ in range(f):
        a, b = sys.stdin.readline().rstrip().split(' ')

        # 없으면
        if not parent.get(a):
            parent[a] = a
            parent_cnt[a] = 1
        if not parent.get(b):
            parent[b] = b
            parent_cnt[b] = 1

        union(a, b)
        p_a = find(a)
        print(parent_cnt[p_a])
