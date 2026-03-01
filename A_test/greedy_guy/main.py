import sys
sys.stdin = open('sample_input.txt','r')

from collections import deque

def dfs(arr,st_p):
    global min_val

    temp_arr = arr[:]

    temp_arr[st_p] = 0
    stack = [st_p]

    while stack:
        pos = stack.pop()

        l_d, r_d = -1,-1

        for l_i in range(pos-1,-1,-1):
            if temp_arr[l_i] == 1:
                l_d = l_i
                break

        for r_i in range(pos+1,N):
            if temp_arr[r_i] == 1:
                r_d = r_i
                break

        if l_d == -1 and r_d == -1:
            min_val = min(min_val, abs(st_p - (M - 1)))
            return

        if l_d != -1 and r_d != -1:
            if abs(pos - l_d) == abs(pos - r_d):
                return
            elif abs(pos - l_d) < abs(pos - r_d):
                stack.append(l_d)
                temp_arr[l_d] = 0
            else:
                stack.append(r_d)
                temp_arr[r_d] = 0

        elif l_d != -1:
            stack.append(l_d)
            temp_arr[l_d] = 0
        elif r_d != -1:
            stack.append(r_d)
            temp_arr[r_d] = 0

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    min_val = float('inf')
    for i in range(N):
        dfs(arr,i)

    print(f'#{tc} {min_val}')