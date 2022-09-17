import sys

A, B = map(int, input().split())
C, D = map(int, input().split())

def gcd(a,b):
    if b == 0:
        return a
    
    return gcd(b,a%b)

result = gcd(A*D + B*C, B*D)
print((A*D + C*B)//result,B*D//result)