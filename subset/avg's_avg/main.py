import sys

sys.stdin = open('sample_input.txt','r')

def find_subset(deps,visited):
    if deps==N:
        temp_list = [ arr[i] for i in range(N) if visited[i] ]
        if temp_list:
            subset_list.append(sum(temp_list)/len(temp_list))
        return

    visited[deps] = True
    find_subset(deps+1,visited)
    visited[deps] = False
    find_subset(deps+1,visited)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    visited = [False] * N
    subset_list = []
    find_subset(0,visited)
    #print(subset_list)

    print(f'#{tc} {sum(subset_list)/len(subset_list)}')