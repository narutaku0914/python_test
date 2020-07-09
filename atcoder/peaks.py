"""
ABC166C

inpit
6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6
"""

N, M = map(int, input().split())

H = list(map(int, input().split()))

# NG = 0, OK = 1
count_list = [1] * N
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    # =のときNGなので、ifを一つ作るか、NG時に0にするように条件付け
    if H[A] >= H[B]:
        count_list[B] = 0
    if H[A] <= H[B]:
        count_list[A] = 0
print(sum(count_list))
    