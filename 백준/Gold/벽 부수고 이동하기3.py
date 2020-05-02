import sys
sys.stdin = open('벽 부수고 이동하기2.txt', 'r')

import sys
input=sys.stdin.readline

di,dj=(0,1,0,-1),(1,0,-1,0)
n,m,k=map(int,input().split())
a=[input().rstrip() for _ in range(n)]
v=[[k+1]*m for _ in range(n)]
v[0][0]=0
def f():
  if n==m==1: return 1
  Q=[(0,0,0)]
  D=1
  while Q:
    D+=1
    q=[]
    for i,j,c in Q:
      for d in range(4):
        I,J=i+di[d],j+dj[d]
        if (I,J)==(n-1,m-1): return D
        if 0<=I<n and 0<=J<m:
          if a[I][J]=='0' and v[I][J]>c:
            v[I][J]=c
            q.append((I,J,c))
          elif a[I][J]=='1' and v[I][J]>c+1 and c<k:
            v[I][J]=c+1
            q.append((I,J,c+1))
    Q=q
  return -1
print(f())
for i in v:
  print(i)