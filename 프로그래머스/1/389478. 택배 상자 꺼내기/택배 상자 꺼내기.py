def solution(n, w, num):
    answer = 0

    # 꺼내려는 상자의 열 위치
    row = (num - 1) // w
    col = (num - 1) % w

    if row % 2 == 1:
        col = w - 1 - col

    # num부터 n까지 같은 열에 있는 상자 확인
    for i in range(num, n + 1):
        r = (i - 1) // w
        c = (i - 1) % w

        if r % 2 == 1:
            c = w - 1 - c

        if c == col:
            answer += 1

    return answer