import heapq
from collections import deque

def solution(jobs):
    # shortest job first
    # 최소힙으로 구현
    jobs_num = len(jobs)
    time_sum = 0
    cur_time = 0    
    jobs.sort()
    jobs = deque(jobs)
    
    wait_queue = []
    while True:        
        while jobs:
            if jobs[0][0] > cur_time:
                if not wait_queue:
                    cur_time = jobs[0][0]
                break
            else:
                next_job, time = jobs.popleft()
                # 해당 job이 수행되기 전
                time_sum += cur_time - next_job
                heapq.heappush(wait_queue, time)            
        
        # 대기중인 작업들이 있다면
        if wait_queue:
            wait_num = len(wait_queue)
            cur_work = heapq.heappop(wait_queue)
            cur_time += cur_work
            time_sum += cur_work * wait_num
        
        if not wait_queue and not jobs:
            break
        
    answer = time_sum // jobs_num
    return answer