import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(deps,total_cal,total_sco):
    global max_val

    if total_cal > L:
        return

    if deps == N:
        max_val = max(max_val,total_sco)
        return

    dfs(deps+1, total_cal + calories[deps], total_sco + scores[deps])
    dfs(deps + 1, total_cal, total_sco)


T = int(input())
for tc in range(1,T+1):
    N, L = map(int, input().split())
    # 정해진 칼로리 이하, 맛에 점수가 가장 높은 값 찾기
    calories = []
    scores = []
    for i in range(N):
        a, b = map(int, input().split())
        calories.append(b)
        scores.append(a)

    max_val = 0
    dfs(0,0,0)
    print(f'#{tc} {max_val}')