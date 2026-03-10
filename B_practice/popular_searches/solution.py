from typing import List
from collections import deque, defaultdict

n = 0
words = deque()
word_cnt = defaultdict(int)

def init(N : int) -> None:
    global n, words, word_cnt
    n = N
    words = deque()
    word_cnt = defaultdict(int)

def addKeyword(mKeyword : str) -> None:
    words.append(mKeyword)
    word_cnt[words] += 1

    if len(words) > n:
        dead_word = words.popleft()
        word_cnt[dead_word] -= 1
        if word_cnt[dead_word] == 0:
            del word_cnt[dead_word]

def top5Keyword(mRet : List[str]) -> int:
    word_list = list(word_cnt.keys())

    similar_word = defaultdict(list)

    for word in word_list:
        for i in range(len(word)-1):
            wild_word = word[:i] + '*' + word[i+1:]
            similar_word[wild_word].append(word)

    parent_data = { word : word for word in word_list }




    return 0
