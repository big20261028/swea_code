import sys
sys.stdin = open('sample_input.txt', 'r')

# 비트마스크를 사용해서 풀어보기
ALL_ALPHABETS = (1 << 26) - 1

def word_to_bit(word):
    bit = 0
    for char in word:
        pos = ord(char) - ord('a')
        bit = bit | (1 << pos)
    return bit


def dfs(deps, subset_word):
    global total

    if subset_word == ALL_ALPHABETS:
        total += (1 << (N - deps))
        return

    if deps == N:
        return

    dfs(deps + 1, subset_word | word_bits[deps])
    dfs(deps + 1, subset_word)


T = int(input())
for tc in range(1, T+1):
    # 광직이가 아는 영어 단어 개수
    N = int(input())
    words = [ input().strip() for _ in range(N) ]

    # 단어를 bit로 변환
    word_bits = [ word_to_bit(word) for word in words ]

    total = 0

    dfs(0,0)

    print(f'#{tc} {total}')


