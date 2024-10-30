# 유클리드 호제법 활용 해보기

a, b = map(int, input().split(' '))

# 6 3
# 1111111 111
if a < b:
    a, b = b, a

answer = 0
while True:
    a, b = a % b, b
    if a < b:
        a, b = b, a

    if b == 0:
        answer = a
        break

print('1'*answer)
