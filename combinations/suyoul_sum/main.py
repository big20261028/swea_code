import sys
sys.stdin = open('sample_input.txt','r')

def find_path_sum(deps,visited):
    global total
    if deps==N:
        temp = 0
        for i in range(N):
            if visited[i]:
                temp += arr[i]
        if temp == K:
            total += 1
        return

    visited[deps] = True
    find_path_sum(deps+1,visited)

    visited[deps] = False
    find_path_sum(deps+1,visited)



T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))
    total = 0
    visited = [False] * N

    find_path_sum(0,visited)

    print(f"#{tc} {total}")