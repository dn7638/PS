import sys
import bisect

input = sys.stdin.readline

N = int(input())
lis = []
seq = list(map(int, input().split()))
trace = []

lis.append(seq[0])
trace.append((0,seq[0]))
for i in range(1,N):
    pos = bisect.bisect_left(lis, seq[i])
    # 0 1 2 3 4 5
    # 1 3 5 2 4 6 9
    # 2 4 5 6 9
    # 1,1 2,3 3,5 1,2 2,4 4,6 5,9
    if len(lis) <= pos:
        trace.append((len(lis), seq[i]))
        lis.append(seq[i])


    else:
        # i번째 수열이 끝이라고 하면 pos 길이의 증가수열임
        lis[pos] = seq[i]
        trace.append((pos, seq[i]))

cur = len(lis) - 1
for i in range(len(trace) - 1, 0, -1):
    if trace[i][0] == cur:
        lis[cur] = trace[i][1]
        cur -= 1

    if cur == -1:
        break
print(len(lis))
print(' '.join(list(map(str,lis))))


# 10 20 10 30 20 50
# 10 20 30
# 1,10 2,20 0,10 3,30