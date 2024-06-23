from collections import deque


def solution(n, lost, reserve):
    answer = []
    stu = [1 for _ in range(n+1)]
    stu[0] = 0
    lost.sort()
    reserve.sort()
    _reserve = list(reserve)
    for idx, x in enumerate(lost):
        stu[x] = 0
    for idx,x in enumerate(reserve):
        if stu[x] == 0:
            stu[x] = 1
            reserve[idx] = 100
            continue
    reserve.sort()
    count = 0
    
    for x in reserve:
        if x > 99:
            break
        
        if x-1 <= 0:
            if stu[x+1] == 0:
                stu[x+1] = 1
        elif x+1 >= n+1:
            if stu[x-1] == 0:
                stu[x-1] = 1
                continue
        else:
            if stu[x-1] == 0:
                stu[x-1] = 1
                continue

            if stu[x+1] == 0:
                stu[x+1] = 1
    
    return sum(stu)