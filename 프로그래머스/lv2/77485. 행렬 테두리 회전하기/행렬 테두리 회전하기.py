from collections import deque

def solution(rows, columns, queries):
    
    N = rows; M = columns
    arr = []
    for n in range(N):
        tmp = []
        for m in range(M):
            tmp.append(m+1 + n*M)
        arr.append(tmp)
        
    result = []
    for q in queries:
        x1, y1, x2, y2 = q; x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
        
        queue = deque([])
        queue.extend(arr[x1][y1:y2+1])
        queue.extend([row[y2] for row in arr[x1+1:x2]])
        queue.extend(arr[x2][y1:y2+1][::-1]) #배열을 완성하고 slicing 해야함
        queue.extend([row[y1] for row in arr[x1+1:x2][::-1]]) #이부분도 배열을 완성하고 slicing 해야함
        
        queue.rotate(1)
        result.append(min(list(queue)))

        for i in range(y1, y2+1):
            arr[x1][i] = queue.popleft()
        for i in range(x1+1, x2):
            arr[i][y2] = queue.popleft()
        for i in range(y2, y1-1, -1):
            arr[x2][i] = queue.popleft()
        for i in range(x2-1, x1, -1):
            arr[i][y1] = queue.popleft()

    return result