n = 9
edges = [[0,2],[2,1],[2,4],[3,5],[5,4],[5,7],[7,6],[6,8]]

need = n// 3
tree = [[] for _ in range(n)]
for a, b in edges:
    tree[a].append(b)
    tree[b].append(a)
start = []
for i in range(len(tree)):
    if len(tree[i]) == 1:
        start.append(i)
start = start + start
answer = []
visitA = [0] * n
visit = [0] * n
for i in start:
    if len(answer) == 2:
        break
    if visitA[i]:
        continue
    for j in range(len(edges)):
        if j in answer:
            continue
        nodeA, nodeB = edges[j]
        stack = [i]
        count = 0
        while stack:
            node = stack.pop()
            visit[node] = 1
            count += 1
            if count > need:
                break
            for k in tree[node]:
                if (node, k) == (nodeA, nodeB) or (k, node) == (nodeA, nodeB):
                    continue
                if visit[k]:
                    continue
                stack.append(k)
        if count == need:
            answer.append(j)
            tree[nodeA].remove(nodeB)
            tree[nodeB].remove(nodeA)
            visitA = visit[:]
            break
        else:
            visit = visitA[:]
print(answer)