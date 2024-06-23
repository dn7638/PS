def solution(clothes):
    dic = {}
    for a, b in clothes:
        if not dic.get(b):
            dic[b] = 2
        else:
            dic[b] += 1
    answer = 1         
    for value in dic.values():
        answer *= value
        
    return answer - 1