from decimal import Decimal, getcontext

getcontext().prec = 30

n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    
    l = Decimal(a) + Decimal(b) ** Decimal('0.5')
    r = Decimal(c) + Decimal(d) ** Decimal('0.5')
    
    if l < r: print("Less")
    elif l == r: print("Equal")
    else: print("Greater")