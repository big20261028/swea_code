import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    n, password = input().split()
    n = int(n)

    #print(n,password)

    # while True:
    #     for i in range(len(password)-1):
    #         if password[i] == password[i+1]:
    #             password = password[:i] + password[i+2:]
    #             break
    #     else:
    #         break

    stack = []
    for char in password:
        if not stack:
            stack.append(char)
            continue

        if stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    result = ''.join(stack)


    print(f'#{tc} {result}')