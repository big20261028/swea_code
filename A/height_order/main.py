import sys
sys.stdin = open('sample_input.txt','r')

from collections import deque
from collections import defaultdict

def bfs(num):
    visited = [True] * (N)
    visited[num-1] = False

    queue = deque([num])
    #count = 0
    # 키 큰사람 수 파악
    while queue:
        student = queue.popleft()
        for std_num in small_dict[student]:
            if visited[std_num - 1]:
                visited[std_num-1] = False
                queue.append(std_num)

    # 키 작은 사람 수 파악
    queue = deque([num])
    while queue:
        student = queue.popleft()
        for std_num in tall_dict[student]:
            if visited[std_num - 1]:
                visited[std_num-1] = False
                queue.append(std_num)

    if True in visited:
        return False
    else:
        return True



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    M = int(input())
    arr = [ list(map(int,input().split())) for _ in range(M) ]

    # key가 value보다 작다
    small_dict = defaultdict(list)
    # key가 value보다 크다
    tall_dict = defaultdict(list)

    for a,b in arr:
        small_dict[a].append(b)
        tall_dict[b].append(a)

    cnt = 0
    for num in range(1,N+1):
        if bfs(num):
            cnt += 1

    print(f'#{tc} {cnt}')
