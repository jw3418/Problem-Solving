def solution(dirs):
    
    d = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}
    
    answer = 0; x = 0; y = 0
    visit = set()
    for dir in dirs:
        nx = x + d[dir][0]; ny = y + d[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (x, y, nx, ny) not in visit and (nx, ny, x, y) not in visit:
                visit.add((x, y, nx, ny)); visit.add((nx, ny, x, y))
                answer += 1
                x = nx; y = ny
            else:
                x = nx; y = ny
                
    return answer