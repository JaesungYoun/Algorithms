import sys

N,K = map(int,sys.stdin.readline().split())

ph = [-1] + list(sys.stdin.readline().strip())

check = [-1] + ([0] * N)
cnt = 0 
for i in range(1,N+1):
    if ph[i] == 'P':
        for j in range(max(1,i-K),i): 
            if ph[j] == 'H' and check[j] == 0:
                check[j] = 1
                cnt += 1
                break
        else:
            for k in range(i+1,min(N+1,i+K+1)):
                if ph[k] == 'H' and check[k] == 0:
                    check[k] = 1
                    cnt += 1
                    break
print(cnt)
                    