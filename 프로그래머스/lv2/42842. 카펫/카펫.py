def solution(brown, yellow):
    
    total = brown + yellow
    width = 3; height = 1
    
    while True:
        height = total // width
        
        if total%width == 0 and width >= height and (width-2)*(height-2) == yellow:
            return[width, height]
        
        width += 1