import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(deps, word_list):
    global total

    if len(set(word_list)) == 26:
        total += 1
        remain = N - deps
        total += 2 ** remain
        return

    if deps == N:
        return

    dfs(deps+1, word_list + words[deps])
    dfs(deps+1, word_list)

T = int(input())
for tc in range(1, T+1):
    # 광직이가 아는 영어 단어 개수
    N = int(input())
    words = [ list(input()) for _ in range(N) ]

    total = 0
    dfs(0,[])
    print(f'#{tc} {total}')
