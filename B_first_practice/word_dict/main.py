import sys
from solution import init, add, move, search, go

CMD_INIT = 100
CMD_ADD = 200
CMD_MOVE = 300
CMD_SEARCH = 400
CMD_GO = 500

def run():
    Q = int(input())
    okay = False
    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            init()
            okay = True
        elif cmd == CMD_ADD:
            mWord = next(input_iter)
            mImportance = int(next(input_iter))
            ans = mWord
            res = add(mWord, mImportance)
            no = int(next(input_iter))
            if res.no != no or res.word != ans:
                okay = False
        elif cmd == CMD_MOVE:
            mDir = int(next(input_iter))
            res = move(mDir)
            no = int(next(input_iter))
            ans = next(input_iter)
            if res.no != no or res.word != ans:
                okay = False
        elif cmd == CMD_SEARCH:
            mStr = next(input_iter)
            res = search(mStr)
            no = int(next(input_iter))
            if res.no != no:
                okay = False
            if no != -1:
                ans = next(input_iter)
                if res.word != ans:
                    okay = False
        elif cmd == CMD_GO:
            mNo = int(next(input_iter))
            res = go(mNo)
            ans = next(input_iter)
            if res.no != mNo or res.word != ans:
                okay = False
        else:
            okay = False
    return okay


sys.stdin = open('sample_input.txt', 'r')

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print("#%d %d" % (tc, score), flush = True)