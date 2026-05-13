def solution(n, words):
    answer = [-1, -1]
    visit = set()
    
    flag = words[0][-1]; visit.add(words[0])
    for i in range(1, len(words)):
        word = words[i]
        if word[0] != flag or word in visit:
            answer[0] = i%n + 1
            answer[1] = i//n + 1
            break
        flag = word[-1]
        visit.add(word)
    
    if answer[0] == -1 and answer[1] == -1:
        answer[0] = 0; answer[1] = 0

    return answer