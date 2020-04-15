heap = [0, 1]

for i in range(2, int(input())+1):
    heap.append(i)  # 맨 뒤에 최댓값 추가
    heap[i], heap[i-1] = heap[i-1], heap[i]
    j = i - 1  # j위치에 있는 최댓값
    while j != 1:  # j위치에 있는 최댓값은 최상단에 위치할 때 까지 부모 노드와 지속적으로 바꾸어줌
        heap[j], heap[j//2] = heap[j//2], heap[j]  # 교환
        j = j//2  # 부모 노드의 위치
print(*heap[1:])