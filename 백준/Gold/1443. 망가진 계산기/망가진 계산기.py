# D 자리까지만 나타남
# P번 2 ~ 9 곱합
# 2 3 4 5 6 7 8 9
# 2 3 2^2 5 2*3 7 2^3 3^2
# 2^a 3^b 5^c 7^d
D, P = map(int, input().split())

visited = {}
result = [-1]
def btk(num, cnt):
    if visited.get((num, cnt)):
        return
    
    visited[(num, cnt)] = True
    
    if cnt > P:
        result[0] = max(result[0], num)
        return

    for i in range(9, 1, -1):
        if num * i < (10**D - 1) and (num * i * 2**(P - cnt)) < 10**D - 1 and (num * i * 9**(P - cnt)) > result[0]:
            btk(num * i, cnt + 1)

if 2**P > 10**D - 1:
    result[0] = -1
elif 9**P < 10**D:
    result[0] = 9**P
else:
    btk(1,1)
print(result[0])
