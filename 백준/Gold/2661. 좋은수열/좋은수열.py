import sys

def check_curr(seq): #"하나의 숫자"를 붙였을 때 좋은 수열을 만족하는 지 확인하는 함수
    n = len(seq)
    for i in range(1, n//2+1):
        if seq[-i:] == seq[-2*i:-i]: return False
    return True

def backtracking(seq):
    if len(seq) == N:
        print(seq); exit() #길이가 N인 좋은 수열을 찾은 경우, 바로 프로세스 종료
    else:
        for i in range(1, 3+1):
            if check_curr(seq+str(i)): #하나의 숫자 붙였을 때 좋은 수열을 만족하는 지 확인
                backtracking(seq+str(i))
    
N = int(sys.stdin.readline()[:-1])
backtracking('1')