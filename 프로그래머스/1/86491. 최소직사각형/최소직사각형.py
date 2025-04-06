def solution(sizes):
    max_W, max_H = 0, 0
    for size in sizes:
        W, H = size
        a_size = max(max_W, W) * max(max_H, H)
        b_size = max(max_W, H) * max(max_H, W)
        if a_size > b_size:
            max_W = max(max_W, H); max_H = max(max_H, W)
        else:
            max_W = max(max_W, W); max_H = max(max_H, H)
    return max_W * max_H