import sys

T = int(sys.stdin.readline())

sieve = [True]* 1000001
prime_arr = []

for i in range(2,1000001):
    if sieve[i]:
        prime_arr.append(i)
        for j in range(2*i,1000001,i):
            sieve[j] = False


for _ in range(T):
    N = int(sys.stdin.readline())
    cnt = 0 
    for i in prime_arr:
        if i > N//2:
            break
        
        if sieve[N-i]:
            cnt += 1
        
            
    print(cnt)