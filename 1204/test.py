scores_list = list(input().split())

print(scores_list)
scores_dict = {}
for score in map(int,scores_list):
    if score in scores_dict:
        scores_dict[score] += 1
    else:
        scores_dict[score] = 1

sorted_scores_dict = dict(sorted(scores_dict.items(),key=lambda x : x[1], reverse=True))
print(sorted_scores_dict)

def many_call_score(scores_list):
    scores_set = set(scores_list)
    many_call_list = []
    max_count = 0

    for item in scores_set:
        if max_count <= scores_list.count(item):
            max_count = scores_list.count(item)
            many_call_list.append(item)
        
    if len(many_call_list) > 1 :
        many_call_list.sort(reverse=True)
        
    # 테스트
    print("="*50)
    print("max_count",max_count)
    print("many_call_list",many_call_list)
    print("="*50)

    return many_call_list[0]