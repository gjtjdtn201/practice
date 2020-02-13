import sys
sys.stdin = open('크로아티아 알파벳.txt', 'r')

word = input()
a = word.replace('c=', 'a')
a = a.replace('c-', 'a')
a = a.replace('dz=', 'a')
a = a.replace('d-', 'a')
a = a.replace('lj', 'a')
a = a.replace('nj', 'a')
a = a.replace('s=', 'a')
a = a.replace('z=', 'a')
print(len(a))