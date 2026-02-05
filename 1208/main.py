def main_logic():
    dump = int(input())
    box_h_list = list(map(int,input().split()))

    for _ in range(dump):
        max_index = box_h_list.index(max(box_h_list))
        min_index = box_h_list.index(min(box_h_list))
        if max_index == min_index:
            break
        box_h_list[max_index] -= 1
        box_h_list[min_index] += 1
    
    result = max(box_h_list) - min(box_h_list)

    return result


text = ""
for i in range(1,11):
    result = main_logic()
    text += f"#{i} {result}\n"
print(text)
