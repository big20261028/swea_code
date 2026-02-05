import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_str = input()

    num_list = []

    max_num = 0
    max_cnt = 0
    for i in range(10):
        cnt = num_str.count((str(i)))
        if max_cnt <= cnt :
            max_cnt = cnt
            max_num = i

    print(f"#{test_case} {max_num} {max_cnt}")
