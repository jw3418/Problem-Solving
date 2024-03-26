from sys import stdin
from collections import defaultdict


def main():
    def input():
        return stdin.readline().rstrip()

    N, d, k, c = map(int, input().split())
    sushis = [int(input()) for _ in range(N)]
    plates = defaultdict(int)
    plates[c] = 1

    cnt = 1
    for i in range(k):
        if plates[sushis[i]] == 0:
            cnt += 1
        plates[sushis[i]] += 1

    res = cnt
    for end in range(k, N + k - 1):
        plates[sushis[end - k]] -= 1
        if plates[sushis[end - k]] == 0:
            cnt -= 1

        plates[sushis[end % N]] += 1
        if plates[sushis[end % N]] == 1:
            cnt += 1

        res = max(cnt, res)

    print(res)


if __name__ == "__main__":
    main()