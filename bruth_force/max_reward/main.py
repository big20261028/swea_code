import sys
sys.stdin = open('input.txt','r')

def dfs(num_list,r):
    global max_val

    if r == 0:
        number = int(''.join(map(str, num_list)))
        if number > max_val:
            max_val = number
        return

    for a in range(num_len):
        for b in range(a+1, num_len):
            temp_list = num_list[:]
            temp_list[a], temp_list[b] = temp_list[b], temp_list[a]
            number = int(''.join(map(str,temp_list)))
            if (number, r - 1) not in visited:
                visited.add((number, r - 1))
                dfs(temp_list,r-1)

    pass

T = int(input())
for tc in range(1,T+1):
    number,r = input().split()
    r = int(r)

    num_list = list(map(int,number))
    num_len = len(number)
    max_val = 0
    visited = set()

    dfs(num_list,r)

    #result = list(visited)

    print(f'#{tc} {max_val}')




