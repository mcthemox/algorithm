# 스택

import sys
input = sys.stdin.readline

num = int(input())

list = []
for i in range(num):
	text = input().split()

	if text[0] == "push":
		list.append(text[1])

	elif text[0] == "top":
		if len(list) == 0:
			print(-1)
		else:
			print(list[-1])

	elif text[0] == "size":
		print(len(list))
	
	elif text[0] == "pop":
		if len(list) == 0:
			print(-1)
		else:
			print(list.pop())
	
	elif text[0] == "empty":
		if len(list) == 0:
			print(1)
		else:
			print(0)