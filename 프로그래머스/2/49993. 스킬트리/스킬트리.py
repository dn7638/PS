def solution(skill, skill_trees):
    skill_graph = {}
    answer = 0
    for i in range(len(skill)-1):
        cur, nxt = skill[i], skill[i+1]
        skill_graph[cur] = nxt
    skill_graph[skill[-1]] = True
    
    for skill_tree in skill_trees:
        cur = skill_tree[0]
        next_seq_skill = skill[0]
            
        for i in range(len(skill_tree)): 
            nxt = skill_tree[i] 
            
            if skill_graph.get(nxt):
                if next_seq_skill != nxt:
                    answer -= 1
                    break
                else:
                    next_seq_skill = skill_graph[nxt]

        answer += 1    
    return answer