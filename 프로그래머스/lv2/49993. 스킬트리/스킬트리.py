def solution(skill, skill_trees):
    
    answer = 0
    for tree in skill_trees:
        step = list(skill); step_set = set(step)
        possible_index = 0
        
        possible_flag = True
        for t in tree:
            if t in step_set:
                if step.index(t) <= possible_index:
                    possible_index = step.index(t) + 1
                else:
                    possible_flag = False; break
                    
        if possible_flag: answer += 1
            
    return answer