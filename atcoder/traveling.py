"""
秒速1
tが奇数のときx, yが奇数でなければ定めた位置にこない
行って来いで2回使うから
"""

N = int(input())

t, x, y = 0, 0, 0

for _ in range(N):
    next_t, next_x, next_y = map(int, input().split())
    diff_t = abs(next_t - t)
    distance = abs(next_x -x) + abs(next_y - y)
    if diff_t > distance:
        if diff_t % 2 == 0 and distance % 2 == 0:
            answer = "Yes"
            t, x, y = next_t, next_x, next_y  
        elif diff_t % 2 != 0 and distance % 2 != 0:
            answer = "Yes"
            t, x, y = next_t, next_x, next_y  
        else:
            answer = "No"
            break
    elif diff_t == distance:
        answer = "Yes"
        t, x, y = next_t, next_x, next_y
    else:
        answer = "No"
        break

print(answer)