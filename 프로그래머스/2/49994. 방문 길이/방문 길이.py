def solution(dirs):
    move = {'U' :(0,1) , 'D' :(0,-1), 'R' :(1,0) , 'L' : (-1,0)}
    graph = [[0 for _ in range(11)] for _ in range(11)]
    s_x, s_y = 5, 5
    way_set = set()
    for inst in dirs:
        dx, dy = move[inst]
        next_x, next_y = s_x + dx, s_y + dy
        if 0<= next_x <= 10 and 0<= next_y <= 10:
            way_set.add((s_x, s_y, next_x, next_y))
            way_set.add((next_x, next_y, s_x, s_y))
            s_x, s_y = next_x, next_y
    
    answer = len(way_set)//2

    return answer