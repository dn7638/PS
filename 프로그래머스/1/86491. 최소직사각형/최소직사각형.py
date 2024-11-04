def solution(sizes):
    max_val = 0
    card_id = 0
    answer = 0
    for idx, item in enumerate(sizes):
        w, h = item[:]
        if w > max_val:
            max_val = w
            card_id = idx
        if h > max_val:
            max_val = h
            card_id = idx
    
    _max_val = min(sizes[card_id])
    for idx, item in enumerate(sizes):
        if idx == card_id:
            continue
        w, h = item[:]
        
        min_val = min(w, h)
        
        if _max_val < min_val:
            _max_val = min_val
    
    answer = max_val * _max_val
        
    
    return answer