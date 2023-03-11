# 스택
import sys
input = sys.stdin.readline

sum = []
n = int(input())
result = 0
for i in range(n):
    text = int(input())
    if text == 0:
        sum.pop()
    else :
        sum.append(text)

if len(sum) == 0:
    print(0)
else :
    for i in range(len(sum)):
        result += sum[i]
    print(result)
