def solution(numbers):
    str_list = list(map(str, numbers))
    _str_list = []
    for idx, x in enumerate(str_list):
        _str_list.append((x*3, x)) 
    _str_list.sort()
    
    re_str_list = []
    
    for x in range(len(str_list)-1,-1,-1):
        re_str_list.append(_str_list[x][1])
    answer = ''.join(re_str_list)
    if int(answer) == 0:
        return str(0)
    return answer

