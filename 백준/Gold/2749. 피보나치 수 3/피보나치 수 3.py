import sys

N = int(sys.stdin.readline()[:-1])
M = 1000000 #10의 7승
P = 15*(10**(6-1)) #주기의 길이

fibo = [0, 1]
for i in range(2, P): #주기의 길이만큼만 fibo를 만듦
    fibo.append(fibo[i-1] + fibo[i-2])
    fibo[i] %= M

print(fibo[N%P])