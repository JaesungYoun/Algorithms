import sys

N, K = map(int, sys.stdin.readline().split())

buy = 0
while bin(N).count('1') > K:
    idx = bin(N)[::-1].index('1')
    buy += 2**idx  #합치기 위해 필요한 최소 물의 양 구입
    N += 2**idx    #물을 합침
    
print(buy)