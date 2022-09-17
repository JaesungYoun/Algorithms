import sys

N = int(sys.stdin.readline())
hp_consume = list(map(int,sys.stdin.readline().split()))
get_joy = list(map(int,sys.stdin.readline().split()))

hp = 100
joy = 0

def dfs(i,hp_now,joy_now):
    global joy
    
    if hp_now <= 0:
        prev_joy = joy_now - get_joy[i-1]
        if prev_joy > joy:
            joy = prev_joy
        return joy
    
    if i == N:
        if joy_now > joy:
            joy = joy_now
        return joy
    
    dfs(i+1,hp_now - hp_consume[i],joy_now + get_joy[i])
    dfs(i+1,hp_now,joy_now)

dfs(0,hp,0)
print(joy)