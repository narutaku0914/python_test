"""
ABC085C

日本でよく使われる紙幣は、10000円札、5000円札1000円札です。以下、「お札」とはこれらのみを指します。
青橋くんが言うには、彼が祖父から受け取ったお年玉袋にはお札が N枚入っていて、合計で Y円だったそうですが、嘘かもしれません。このような状況がありうるか判定し、
ありうる場合はお年玉袋の中身の候補を一つ見つけてください。なお、彼の祖父は十分裕福であり、お年玉袋は十分大きかったものとします。
"""


def countBills(n, y):
    bills_list = ["-1", "-1", "-1"]
    for i in range(n+1):
        for j in range(n+1):
            # 2変数決まればあとはnに合うように1変数決める
            k = n - (i + j)
            if k >= 0 and (10000 * i + 5000 * j + 1000 * k) == y:
                bills_list = [str(i), str(j), str(k)]
                break
    return bills_list


n, y = map(int, input().split())
print(" ".join(countBills(n, y)))
