def solution(n):
    bin_n = list(bin(n)[2:])
    one_cnt = bin_n.count('1')
    
    if one_cnt == len(bin_n):
        answer = [1] * (len(bin_n)+1); answer[1] = 0
        return int(''.join(map(str, answer)), 2)
    else:
        while True: #n에 1을 더해주면서 조건을 만족하는 가장 작은 수 출력
            n += 1
            if list(bin(n)[2:]).count('1') == one_cnt:
                return int(''.join(map(str, bin(n)[2:])), 2)