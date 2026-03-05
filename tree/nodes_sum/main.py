import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    node_list = [0] * (N + 1)
    node_dict = {}
    for _ in range(M):
        p, c = map(int, input().split())
        node_list[p] = c
        node_dict[p] = c

    while node_dict:
        temp_dict = {}

        for key,val in node_dict.copy().items():
            parent_key = key // 2
            if parent_key == 0: break
            node_list[parent_key] += val
            if parent_key in temp_dict:
                temp_dict[parent_key] += val
            else:
                temp_dict[parent_key] = val

        node_dict = temp_dict

    #print(node_list)
    print(f'#{tc} {node_list[L]}')
