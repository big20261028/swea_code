import sys
sys.stdin = open('input.txt','r')

# 키의 크기의 조합을 구하는 부분집합
# if total이 B보다 크면 즉시 종료

def tools(deps,include):
    if deps == N:
        # 포함 여부가 True인 인덱스만 넣기
        result = [ heights[i] for i in range(N) if include[i] ]
        h = sum(result)
        if h >= B:
            diff_list.append(h-B)
        return

    include[deps] = False
    tools(deps+1,include)

    include[deps] = True
    tools(deps+1,include)

T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    heights = list(map(int,input().split()))
    #min_diff = 0
    # 부분집합 구현을 위한 flag 리스트 생성
    include = [False] * N
    diff_list = []
    tools(0,include)
    min_diff = min(diff_list)

    print(f'#{tc} {min_diff}')




