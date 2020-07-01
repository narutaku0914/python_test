n = 5
p = 4


pages = []
for i in range(0, n+1, 2):
    pages.append((i, i+1))

if p % 2 == 0:
    pages_count = pages.index((p, p+1))
else:
    pages_count = pages.index((p-1, p))

pages_r = pages[::-1]
if p % 2 == 0:
    pages_r_count = pages_r.index((p, p+1))
else:
    pages_r_count = pages_r.index((p-1, p))

if pages_count <= pages_r_count:
    result = pages_count
else:
    result = pages_r_count

print(result)
