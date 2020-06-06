#Find Remainder. Link - https://www.codechef.com/problems/FLOW002

T = int(raw_input())
for tc in range(T):
	(a, b) = map(int, raw_input().split(' '))
	ans = a%b
	print(ans)
