def insu(n):
    insu = []
    division = 2
    while True:
        if division * division > n:
            insu.append(n)
            break
        if n % division == 0:
            insu.append(division)
            n = n // division
            division = 2
        else:
            division += 1
    return insu

N = int(input())
a_insu = {}
for i in map(int, input().split(' ')):
    temp_insu = insu(i)
    for j in temp_insu:
        if a_insu.get(j):
            a_insu[j] += 1
        else:
            a_insu[j] = 1

M = int(input())
b_insu = {}
for i in map(int, input().split(' ')):
    temp_insu = insu(i)
    for j in temp_insu:
        if b_insu.get(j):
            b_insu[j] += 1
        else:
            b_insu[j] = 1

answer = 1
for key, value in b_insu.items():
    if a_insu.get(key):
        for _ in range(min(a_insu[key], b_insu[key])):
            answer *= key

if len(str(answer))>9:
    print(str(answer)[-9:])
else:
    print(answer)

