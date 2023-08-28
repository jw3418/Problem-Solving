def solution(order):
    N = len(order)
    
    belt = [i for i in range(1, N+1)]
    a_belt = [] #보조 컨테이너 벨트
    
    b_idx = 0; count = 0
    for o_idx in range(N):
        if b_idx < N and order[o_idx] == belt[b_idx]: 
            b_idx += 1
            count += 1
        else:
            if a_belt and a_belt[-1] == order[o_idx]: #a_belt의 tail이 마침 일치하는 경우
                count += 1
                a_belt.pop()
            
            elif b_idx < N: #보조 컨테이너 벨트에 옮길 수 있는 경우
                while True:
                    a_belt.append(belt[b_idx])
                    b_idx += 1
                    if b_idx >= N:
                        break
                    if order[o_idx] == belt[b_idx]: #보조 컨테이너 벨트에 옮기다가 트럭에 실을 수 있는 경우 발견
                        b_idx += 1
                        count += 1
                        break
            else:
                break
                    
    return count