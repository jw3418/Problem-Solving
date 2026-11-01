def solution(video_len, pos, op_start, op_end, commands):
    video_len = int(video_len[0:2]) * 60 + int(video_len[3:5])
    pos = int(pos[0:2]) * 60 + int(pos[3:5])
    op_start = int(op_start[0:2]) * 60 + int(op_start[3:5]); op_end = int(op_end[0:2]) * 60 + int(op_end[3:5])
    print(video_len, pos, op_start, op_end)
    
    for _ in range(len(commands)):
        if op_start <= pos <= op_end: pos = op_end
        
        if commands[_] == "next":
            pos += 10
            if pos > video_len:
                pos = video_len
        elif commands[_] == "prev":
            pos -= 10
            if pos < 0:
                pos = 0
        if op_start <= pos <= op_end: pos = op_end

    front = str(pos//60)
    if len(front) == 1: front = "0" + front
    back = str(pos%60)
    if len(back) == 1: back = "0" + back
    answer = front + ":" + back
    
    return answer