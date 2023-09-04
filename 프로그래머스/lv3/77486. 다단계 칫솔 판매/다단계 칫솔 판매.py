def solution(enroll, referral, seller, amount):
    N = len(enroll)
    
    graph = dict() #key:child, value:parent
    for i in range(N): graph[enroll[i]] = referral[i]
        
    all_profit = dict()
    for i in range(N): all_profit[enroll[i]] = 0
        
    def distribute(node, profit):
        if profit // 10 == 0:
            all_profit[node] += profit
            return
        
        tax = profit // 10
        all_profit[node] += profit - tax
        
        if graph[node] != '-':
            distribute(graph[node], tax)

    M = len(seller)
    for i in range(M): distribute(seller[i], amount[i]*100)
    
    return list(all_profit.values())