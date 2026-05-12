def solution(arr1, arr2):
    N = len(arr1); M = len(arr1[0]); K = len(arr2[0])
    answer = [[-1 for _ in range(K)] for _ in range(N)]
    
    for i in range(N):
        for j in range(K):
            total = 0
            for m in range(M):
                total += arr1[i][m] * arr2[m][j]
            answer[i][j] = total
    return answer