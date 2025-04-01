def solution(phone_book):
    N = len(phone_book)
    
    phone_book.sort(key=lambda x:len(x))
    set_ = set()
    for i in range(N):
        tmp = ""
        for j in range(len(phone_book[i])):
            tmp += phone_book[i][j]
            if tmp in set_: return False
        set_.add(phone_book[i])
    return True