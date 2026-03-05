import sys
sys.stdin = open('sample_input.txt','r')

def find_subset(deps,visited):
    global total
    if deps == 12:
        temp = [ arr[i] for i in range(12) if visited[i] ]
        if len(temp) == N and sum(temp) == K:
            total += 1
        return

    visited[deps] = True
    find_subset(deps+1,visited)
    visited[deps] = False
    find_subset(deps+1,visited)

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())

    arr = [ i for i in range(1,13) ]
    visited = [False] * 12
    total = 0
    find_subset(0,visited)

    print(f'#{tc} {total}')