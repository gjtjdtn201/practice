import sys
sys.stdin = open("정곤이의 단조 증가하는 수.txt", "r")

T = int(input())

for test_case in range(1, T+1):
	N = int(input())
	ml = list(map(int, input().split()))
	ans = -1
	for i in range(N-1):
		for z in range(i+1, N):
			a = ml[i]*ml[z]
			b = list(str(a))
			if len(b) > 1:
				for j in range(len(b)-1):
					if b[j] > b[j+1]:
						break
				else:
					if ans < a:
						ans = a
			elif ans < a:
				ans = a

	print('#{} {}'.format(test_case, ans))