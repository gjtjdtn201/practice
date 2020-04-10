# 단일(단순) 연결 리스트
class Node:
    def __init__(self, d=0, n=None):
        self.data = d           # 정수 값
        self.next = n           # 다음 노드 주소

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

mylist = linkedlist()

def printList(lst):
    if lst.head is None:
        return
    cur = lst.head

    print(lst.size, '[', end=' ')
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next
    print(']')

def insertLast(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        lst.tail.next = new
        lst.tail = new

    lst.size += 1

def deleteLast(lst):
    if lst.head is None:
        return
    pre, cur = None, lst.head
    while cur.next is not None:
        pre = cur
        cur = cur.next
    # 빈 리스트 일 경우
    if pre is None:
        lst.head = lst.tail = None
    else:
        pre.next = None
        lst.tail = pre
    lst.size -= 1

def insertFirst(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new

    lst.size += 1

def deleteFirst(lst):
    if lst.head is None:
        return
    # 노드가 1개일 경우를 주의한다.
    lst.head = lst.head.next
    if lst.head is None:
        lst.tail = None
    lst.size -= 1

def insertAt(lst, idx, new):        # idx : 인덱스값
    # 빈리스트일 경우, idx == 0
    if lst.head is None or idx == 0:
        insertFirst(lst, new)
    # 마지막에 추가하는 경우 idx >= lst.size
    elif idx >= lst.size:
        insertLast(lst, new)
    # 중간에 추가하는 경우
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
        lst.size += 1

def deleteAt(lst, idx):
    # 빈리스트일 경우
    if lst.tail is None or idx == 0:
        deleteFirst(lst)
    # 마지막을 삭제 경우
    elif idx == lst.size:
        deleteLast()
    # 중간을 삭제하는 경우
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        lst.size -= 1


for i in range(5):
    insertFirst(mylist, Node(i))
    printList(mylist)

for i in range(3):
    insertAt(mylist, 2, Node(i+10))
    printList(mylist)