import sys
import bisect

input = sys.stdin.readline

N = int(input())

lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()
lis = []

# lines[i][0] = A번호
# lines[i][1] = B번호

# 1 2 3 4 5
#           pos = 5
trace = [-1 for _ in range(500001)]
index_list = []

for i in range(len(lines)):
    A, B = lines[i][:]

    if not lis:
        lis.append(B)
        trace[B] = 0
        continue

    pos = bisect.bisect_left(lis, B)
    if pos >= len(lis):
        trace[B] = len(lis)
        lis.append(B)

    else:
        lis[pos] = B
        trace[B] = pos

line_B = set()
print(N - len(lis))

# trace 배열을 역순으로 참조
# 조회 및 cur--
# trace 의 인덱스가 B
# 5 4 3 .... 1 0 까지 역순으로 제일 먼저 만나는것들이 lis 중 하나
# trace 배열은 0 0 0 0 x 1 1 x 2 3 x x x 3 3 4 4 5 ... 이런식임
cur = len(lis) - 1
for i in range(len(trace) - 1, 0, -1):
    if trace[i] == cur:
        lis[cur] = i
        cur -= 1

    if cur == -1:
        break

for b in lis:
    line_B.add(b)

for i in range(N):
    if not (lines[i][1] in line_B):
        print(lines[i][0])