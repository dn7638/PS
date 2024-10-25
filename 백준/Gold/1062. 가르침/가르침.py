import itertools

# k글자 -> 읽을 수 있는 단어 최대한

# anta - tica
# aaacntti -> 5
# 남극언어 N

n, k = map(int, input().split(' '))
# k개보다 큰 경우 a c n t i 포함
_words = [list(input().rstrip()) for _ in range(n)]
words = [i[4:-4] for i in _words]

alpha = [
    'b', 'd', 'e',
    'f', 'g', 'h', 'j',
    'k', 'l', 'm', 'o',
    'p', 'q', 'r', 's',
    'u', 'v', 'w', 'x', 'y', 'z'
]

default_alph = ['a', 'c', 'n', 't', 'i']

# 알파벳 : 21개 + 5 개
# 21C10 = 35만 * 50 * 10

# k 개의 글자
total_cnt = 0
if k < 5:
    print(0)
else:
    # k - 5 개 선택, 5개는 무조건 있는것
    # 26개중에 k개 선택
    # 21개중에 k'개 선택
    # 21개중에 안가르칠 글자수 21 - k + 5
    # 26 - k

    # 'a', 'c', 'n', 't' ,'i'

    cases = list(itertools.combinations(alpha, 26 - k))

    for case in cases:

        cnt = n
        a = set(case)
        for word in words:
            for ch in word:
                if ch in a:
                    cnt -= 1
                    break
        if total_cnt < cnt:
            total_cnt = cnt

    print(total_cnt)
