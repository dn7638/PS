def solution(progresses, speeds):
    answer = []
    cur = 0
    
    while cur < len(progresses):
        cnt = (100 - progresses[cur])//speeds[cur]
        if (100 - progresses[cur]) % speeds[cur] != 0:
            cnt += 1

        for i in range(len(progresses)):
            progresses[i] += speeds[i] * cnt

        num = 0
        for i in range(cur, len(progresses)):
            if progresses[i] >= 100:
                num += 1
            else:
                break
        answer.append(num)
        cur += num
    
    
    return answer