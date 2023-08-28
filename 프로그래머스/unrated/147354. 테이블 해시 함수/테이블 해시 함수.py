def solution(data, col, row_begin, row_end):
    col -= 1; row_begin -= 1; row_end -= 1
    R = len(data); C = len(data[0])
    
    data.sort(key=lambda x: x[0], reverse=True)
    data.sort(key=lambda x: x[col])
    
    hs = 0
    for r in range(row_begin, row_end+1):
        tmp = 0
        for c in range(C):
            tmp += data[r][c] % (r+1)
        hs = hs ^ tmp
    return hs