import sys
sys.stdin = open('sample_input.txt', 'r')

dxy = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

def dfs(i, j):
    global nums
    #visited = [[False] * 4 for _ in range(4)]
    stack = [[(i, j), [matrix[i][j]]]]

    while stack:
        (x, y), num_list = stack.pop()
        if len(num_list) >= 7:
            nums.add(tuple(num_list))
            continue

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < 4 and 0 <= ny < 4):
                continue
            stack.append([(nx, ny), num_list + [matrix[nx][ny]]])


T = int(input())
for tc in range(1, T+1):
    matrix = [ list(map(int,input().split())) for _ in range(4) ]

    nums = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j)

    print(f'#{tc} {len(nums)}')