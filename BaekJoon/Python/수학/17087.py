import sys

N,S = map(int,sys.stdin.readline().split())

ds = list(map(int,sys.stdin.readline().split()))


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)


d = abs(S-ds[0])

for i in range(1,len(ds)):
    d = gcd(abs(S - ds[i]),d)

print(d)
    