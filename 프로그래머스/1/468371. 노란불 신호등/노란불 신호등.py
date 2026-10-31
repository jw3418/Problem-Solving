from math import gcd

def solution(signals):
    answer = -1

    # 1. 모든 신호등 주기의 최소공배수 계산
    lcm = 1

    for G, Y, R in signals:
        period = G + Y + R
        lcm = lcm * period // gcd(lcm, period)

    # 2. 1초부터 전체 반복 주기까지 탐색
    for t in range(1, lcm + 1):
        all_yellow = True

        for G, Y, R in signals:
            period = G + Y + R
            current = (t - 1) % period

            # 노란불이 아닌 경우
            if not (G <= current < G + Y):
                all_yellow = False
                break

        if all_yellow:
            return t

    return -1