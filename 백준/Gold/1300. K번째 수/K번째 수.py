import sys
input = sys.stdin.readline

'''
이분탐색을 통해 어떤 수보다 작은 자연수의 곱 (i*j)이 몇개인지 알아내야함
10*10의 2차원 배열에서, 20보다 작은 수의 개수는 아래와 같음

1*1 1*2 1*3 1*4 1*5 1*6 1*7 1*8 1*9 1*10
2*1 2*2 2*3 2*4 2*5 2*6 2*7 2*8 2*9 2*10
3*1 3*2 3*3 3*4 3*5 3*6
...
10*1 10*2

==> 20을 행으로 나눈 몫 (단, 최대 열의 개수)
'''

N = int(input()); k = int(input())

l, r = 1, N*N
ans = 0
while l <= r:
    mid = (l+r)//2 #B[k]

    cnt = 0
    for i in range(1, N+1): cnt += min(mid//i, N)

    if cnt >= k:
        ans = mid
        r = mid-1
    else:
        l = mid+1
print(ans)