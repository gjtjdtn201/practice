# 보이어 무어 알고리즘
for t in range(int(input())):
    pattern = input()
    text = input()
    pivot = len(pattern)-1
    skip_array = list(pattern)
    skip_array.reverse()
    result = 0
    while result != 1 and pivot < len(text):
        if pattern[len(pattern)-1] != text[pivot]:
            if text[pivot] in skip_array:
                nums = skip_array.index(text[pivot])
                pivot += nums
            else:
                pivot += len(pattern)
        else:
            for i, j in zip(range(pivot, pivot-len(pattern), -1), skip_array):
                if text[i] == j:
                    result = 1
                else:
                    result = 0
                    pivot = i
                    break
    print("#{} {}".format(t+1, result))