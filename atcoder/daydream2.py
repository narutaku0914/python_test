"""
ABC049C
"""

"""
アプローチ 末尾から読み込めば、あってなければNO出るし、~erの場合分けもできる！
前回はおそすぎた
"""

string = input()

while len(string) >= 5:
    if string[-2:] == "er":
        if string[-6:] == "eraser":
            string = string[:-6]
        elif string[-7:] == "dreamer":
            string = string[:-7]
        else:
            break
    elif string[-5:] == "dream" or string[-5:] == "erase":
        string = string[:-5]
    else:
        break

if len(string) == 0:
    print("YES")
else:
    print("NO")

