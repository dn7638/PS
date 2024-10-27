import sys
import heapq

input = sys.stdin.readline

n = int(input())
left = [] # max heap
right = []
heapq.heapify(left)
heapq.heapify(right)

if n == 1:
    num = int(input())
    print(num)

else:
    mid = int(input())
    print(mid) 
    left_cnt, right_cnt = 0, 0
    for i in range(1,n):
        num = int(input())
        # [] mid []
        # [] mid [3]
        # [1 2] mid [4 5]
        # [1] mid [3 4]
        if mid < num:
            heapq.heappush(right, num)
            right_cnt += 1

            if left_cnt + 2 == right_cnt:
                heapq.heappush(left, -mid)
                left_cnt += 1
                mid = heapq.heappop(right)
                right_cnt -= 1
        else:
            heapq.heappush(left, -num)
            left_cnt += 1
            if left_cnt == right_cnt + 1:
                heapq.heappush(right, mid)
                right_cnt += 1
                mid = -heapq.heappop(left)
                left_cnt -= 1
        
        print(mid)
