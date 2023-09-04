def solution(cards):
    N = len(cards) # cards에는 N이하의 자연수가 들어있음
    
    count = []; openned = set()
    for i in range(N):
        if cards[i] not in openned:
            tmp_count = 1
            openned.add(cards[i]); nidx = cards[i]-1
            while True:
                if cards[nidx] in openned: break
                tmp_count += 1; openned.add(cards[nidx]); nidx = cards[nidx]-1
            count.append(tmp_count)
        
    if count[0] == N: return 0

    count.sort(reverse=True)
    return count[0]*count[1]