n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

num_dict = {}
for i in range(n):
    if not ar[i] in num_dict:
        num_dict[ar[i]] = 1
    else:
        num_dict[ar[i]] += 1

pair_count = 0
while True:
    if num_dict:
        for k in list(num_dict):
            if num_dict[k] > 1:
                num_dict[k] = num_dict[k] - 2
                pair_count += 1
            else:
                num_dict.pop(k)
    else:
        break

print(pair_count)