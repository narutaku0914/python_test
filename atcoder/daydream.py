"""
ABC049C
"""

"""
string = "apple"
string = string.rstrip(string[-2:])
# string_ = string[-3:-1]
print(string[-3:] == "app")
"""
"""
アプローチ 末尾から読み込めば、あってなければNO出るし、~erの場合分けもできる！
"""

string = input()

while True:
    if string == "":
        answer = "YES"
        break

    if string[-2:] == "er":
        if string[-6:] == "eraser":
            string = string[:-6]
        elif string[-7:] == "dreamer":
            string = string[:-7]
        else:
            answer = "NO"
    elif string[-5:] == "dream" or string[-5:] == "erase":
        string = string[:-5]
    else:
        answer = "NO"
        break

print(answer)

