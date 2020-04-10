import sys
sys.stdin = open('암호.txt', 'r')

class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

def addLast(lst, new):
    if lst.head is None:
        lst.head = new
        new.prev = new.next = new
    else:
        tail = lst.head.prev
        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new
    lst.size += 1

def printList(lst):
    if lst.head is None:
        return
    cur = lst.head.prev
    cnt = 0
    for _ in range(lst.size):
        cnt += 1
        if cnt == 11:
            break
        print(cur.data, end=' ')
        cur = cur.prev
    print()

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    mylist = LinkedList()
    arr = list(map(int, input().split()))
    for val in arr:
        addLast(mylist, Node(val))

    cur = mylist.head
    for _ in range(K):
        for __ in range(M):
            cur = cur.next
        prev = cur.prev
        new = Node(prev.data + cur.data, prev, cur)
        prev.next = new
        cur.prev = new
        cur = new       # 새로 추가된 위치를 시작위치로 재설정
        mylist.size += 1
    print('#{} '.format(tc), end='')
    printList(mylist)