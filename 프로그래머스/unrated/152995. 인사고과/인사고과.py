def solution(scores):
    target_a, target_b = scores[0]; target_score = sum(scores[0])
    scores.sort(key=lambda x: (-x[0], x[1])) #근무태도점수에 대해 내림차순, 동료평가점수에 대해 오름차순 정렬
    max_b = 0
    
    answer = 1
    for a, b in scores:
        if target_a < a and target_b < b: return -1
        if b >= max_b:
            max_b = b
            if a + b > target_score:
                answer += 1
    return answer