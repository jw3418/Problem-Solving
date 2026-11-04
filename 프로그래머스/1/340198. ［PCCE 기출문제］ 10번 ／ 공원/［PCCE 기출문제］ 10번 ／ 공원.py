def solution(mats, park):
    N = len(park); M = len(park[0])
    mats.sort(reverse=True)
    
    for size in mats:
        if size > N or size > M: continue
        
        for i in range(N-size+1):
            for j in range(M-size+1):
                
                flag = True
                
                for x in range(i, i+size):
                    for y in range(j, j+size):
                        if park[x][y] != "-1":
                            flag = False
                            break
                
                if flag: return size
    
    return -1