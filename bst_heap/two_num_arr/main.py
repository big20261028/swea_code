import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) > len(B):
        A, B = B, A

    answer = max(sum(A[j] * B[i + j] for j in range(len(A))) for i in range(len(B) - len(A) + 1))

    print(f"#{tc} {answer}")