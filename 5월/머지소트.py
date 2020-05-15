def merge(list1, list2):
    global cnt
    i = 0
    j = 0
    merged_list = []
    if list1[-1] > list2[-1]:
        cnt += 1
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    mid = len(my_list)//2
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])
    return merge(left, right)

for tc in range(1, int(input())+1):
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    b = merge_sort(a)
    print('#{} {} {}'.format(tc, b[N//2], cnt))