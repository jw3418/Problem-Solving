def solution(book_time):
    N = len(book_time)
    
    for i in range(N):
        for j in range(2):
            tmp = list(map(int, book_time[i][j].split(':')))
            book_time[i][j] = tmp[0]*60 + tmp[1]
    book_time.sort(key=lambda x: x[0])
    
    rooms = []
    rooms.append(book_time[0][1])
    for i in range(1, N):
        
        flag = False
        for j in range(len(rooms)):
            if rooms[j] + 10 <= book_time[i][0]:
                rooms[j] = book_time[i][1]
                flag = True; break
        if not flag:
            rooms.append(book_time[i][1])
    
    return len(rooms)