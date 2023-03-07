import sys
input = sys.stdin.readline
list = []

N =  int(input())
for _ in range(N):
    list.append(int(input()))
listed = sorted(list)
for i in range(0,len(listed)):
    print(listed[i])
