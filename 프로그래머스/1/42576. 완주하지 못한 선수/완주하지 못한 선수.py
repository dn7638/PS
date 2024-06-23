def solution(participant, completion):
    dic = dict()
    
    for i in participant:
        if not dic.get(i):
            dic[i] = 1
        else:
            dic[i] += 1
            
    for i in completion:
        dic[i] -= 1
        
            
    for key, value in dic.items():
        if value == 1:
            return key