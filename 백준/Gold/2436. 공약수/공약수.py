
최대공약수, 최소공배수 = map(int, input().split(' '))

# 합이 최소가 되는 두 수

# A, B = 최대공약수의 배수
# 6a, 6b
# a, b 는 서로소
# a * b * 최대공약수 = 최소공배수

# 소인수 분해
def soinsu(n):
    insu = set()
    a = 2
    while True:
        if a * a > n:
            break
        if n % a == 0:
            # 인수임
            b = num // a
            insu.add((a, b))
        a += 1

    return insu


num = 최소공배수 // 최대공약수

answer_list = []
for a in range(1, num +1):
    if num % a != 0:
        continue

    b = num // a
    if b < a:
        break

    set_a = soinsu(a)
    set_b = soinsu(b)

    is_srs = True
    while set_a:
        _a = set_a.pop()
        if _a in set_b:
            is_srs = False
            break

    if is_srs:
        answer_list.append(( a +b, a, b))

answer_list.sort()
print(answer_list[0][1] * 최대공약수 ,answer_list[0][2] * 최대공약수 )
