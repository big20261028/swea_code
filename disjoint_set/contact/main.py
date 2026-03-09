import sys
sys.stdin = open('input.txt', 'r')

from collections import defaultdict, deque

def bfs(st_n):
    global max_val, max_deps

    queue = deque()
    queue.append( (st_n, 0))
    visited = [st_n]

    while queue:
        n, deps = queue.popleft()
        if deps > max_deps:
            max_deps = deps
            max_val = n
        elif deps == max_deps:
            max_val = max(max_val, n)

        for next_n in dict_data[n]:
            if next_n in visited: continue
            visited.append(next_n)
            queue.append( (next_n, deps+1))



for tc in range(1,11):
    N, S = map(int,input().split())
    arr = list(map(int,input().split()))
    dict_data = defaultdict(list) # 연락자 key => 수신자 value
    for i in range(N//2):
        from_i = arr[i*2]
        to_i = arr[i*2 + 1]
        dict_data[from_i].append(to_i)

    #print(dict_data)

    max_deps = 0
    max_val = 0

    bfs(S)

    print(f'#{tc} {max_val}')