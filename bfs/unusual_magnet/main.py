import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnets = [ deque(list(map(int,input().split()))) for _ in range(4) ]
    orders = [ list(map(int,input().split())) for _ in range(K)]

    for target, r in orders:
        queue = deque()
        queue.append([target-1, r])

        roll_data = [0] * 4
        visited = [False] * 4
        visited[target-1] = True

        while queue:
            mag_idx, dirt = queue.popleft()

            if mag_idx < 3:
                if not visited[mag_idx + 1]:
                    if magnets[mag_idx][2] != magnets[mag_idx+1][6]:
                        visited[mag_idx + 1] = True
                        queue.append([mag_idx+1, -dirt])

            if mag_idx > 0:
                if not visited[mag_idx - 1]:
                    if magnets[mag_idx][6] != magnets[mag_idx - 1][2]:
                        visited[mag_idx - 1] = True
                        queue.append([mag_idx - 1, -dirt])

            if dirt > 0:
                temp = magnets[mag_idx].pop()
                magnets[mag_idx].appendleft(temp)
            elif dirt < 0 :
                temp = magnets[mag_idx].popleft()
                magnets[mag_idx].append(temp)

    #print(magnets)
    score = 0
    for i in range(4):
        if magnets[i][0] == 1:
            score += 2 ** i

    print(f'#{tc} {score}')