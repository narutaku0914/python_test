"""
ABC160C問題

input
20 3
0 5 15
"""

K, N = map(int, input().split())

A = list(map(int,input().split()))

dist_list = []
dist_list.append(K - A[N-1] + A[0]) # またいでる部分の計算

for i in range(1, N):
  dist_list.append(A[i]-A[i-1])
dist_list.remove(max(dist_list))

print(sum(dist_list))