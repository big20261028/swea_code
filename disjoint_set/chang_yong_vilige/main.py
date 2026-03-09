import sys
sys.stdin = open('s_input.txt', 'r')

def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]

def union(a,b):
    px = find(a)
    py = find(b)

    if rank[px] > rank[py]:
        p[py] = px
    elif rank[py] > rank[px]:
        p[px] = py
    else:
        p[py] = px
        rank[px] += 1


T = int(input())
for tc in range(1,T+1):
    # 사람수, 관계수
    N, M = map(int,input().split())

    p = [ i for i in range(N+1) ]
    rank = [0] * (N+1)

    for i in range(M):
        a,b = map(int,input().split())
        union(a,b)

    for i in range(1,N+1):
        find(i)

    set_data = set(p)
    #print(set_data)

    print(f'#{tc} {len(set_data) - 1}')

