from collections import deque

def solution(tickets):
    tickets.sort()
    visit = [False]*len(tickets)

    def dfs(src, path):
        if len(path) == len(tickets)+1:
            answer.append(path)
            return

        for i in range(len(tickets)):
            if src == tickets[i][0] and not visit[i]:
                visit[i] = True
                dfs(tickets[i][1], path+[tickets[i][1]])
                visit[i] = False #백트래킹

    answer = []
    dfs('ICN', ['ICN'])
    return answer[0]