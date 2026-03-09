import sys
sys.stdin = open('sample_input.txt', 'r')

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
        p[px] = py
        rank[py] += 1

T = int(input())
for tc in range(1,T+1):
    # 원소 갯수, 연산 개수
    N, M = map(int,input().split())

    p = [ i for i in range(N + 1) ]
    rank = [0] * (N + 1)

    #orders = [ set(map(int,input().split())), for _ in range() ]
    result = ''
    for i in range(M):
        order, a, b = map(int,input().split())

        if not order: # order가 0인 경우
            union(a,b)
        else:
            if find(a) == find(b):
                result += '1'
            else:
                result += '0'

    print(f'#{tc} {result}')


