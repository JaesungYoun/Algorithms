import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    prices = list(map(int,sys.stdin.readline().split()))
    stock = 0
    max_val = prices[-1]
    
    for i in range(len(prices)-1,-1,-1):
        if prices[i] > max_val:
            max_val = prices[i]
        else:
            stock += max_val - prices[i]
            
    print(stock)
                