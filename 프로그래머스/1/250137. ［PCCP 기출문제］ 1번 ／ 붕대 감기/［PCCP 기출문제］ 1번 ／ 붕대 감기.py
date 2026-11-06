def solution(bandage, health, attacks):
    T = attacks[-1][0]
    
    attack_dict = dict()
    for attack in attacks:
        attack_dict[attack[0]] = attack[1]
    
    max_health = health; cur_health = health; strick = 0
    for t in range(1, T+1):
        if t in attack_dict:
            cur_health -= attack_dict[t]
            if cur_health <= 0: return -1
            strick = 0
        else:
            cur_health += bandage[1]
            strick += 1
            if strick == bandage[0]:
                cur_health += bandage[2]
                strick = 0
            cur_health = min(cur_health, max_health)   
        print(t, cur_health, strick)
    return cur_health
    