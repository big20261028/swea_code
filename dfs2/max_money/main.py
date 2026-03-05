import sys
sys.stdin = open('input.txt', 'r')

def dfs(deps,num_list):
    global max_val
    if deps == R:
        val = int(''.join(num_list))
        max_val = max(max_val, val)
        return


    for idx_1 in range(len(st_num_list)):
        for idx_2 in range(idx_1+1, len(st_num_list)):
            temp_list = num_list[:]
            temp_list[idx_1], temp_list[idx_2] = temp_list[idx_2], temp_list[idx_1]
            if (tuple(temp_list), deps) in visited:
                continue
            visited.add((tuple(temp_list), deps))
            dfs(deps+1, temp_list)


T = int(input())
for tc in range(1, T+1):
    nums, R = map(int, input().split())
    max_val = 0
    st_num_list = list(str(nums))

    visited = set()

    dfs(0, st_num_list)

    print(f'#{tc} {max_val}')