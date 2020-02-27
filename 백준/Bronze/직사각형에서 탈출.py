import sys
sys.stdin = open('직사각형에서 탈출.txt', 'r')

x, y, w, h = map(int, input().split())
print(min(min(w-x, x), min(h-y, y)))