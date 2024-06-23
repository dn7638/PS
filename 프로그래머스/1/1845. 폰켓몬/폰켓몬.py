def solution(nums):
    종류 = [0 for _ in range(200001)]
    for x in nums:
        종류[x] = 1
        
    answer = min(sum(종류), len(nums)//2)

    return answer