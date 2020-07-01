"""
removeは、対象の文字のはじめのindexが削除される
"""
"""
input
6 4
give me one grand today night
give one grand today
"""

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    for word in note:
        if note.count(word) <= magazine.count(word):
            answer = "Yes"
            note = list(filter(lambda x: x != word, note))  # filter(func, object)
        else:
            answer = "No"
            break
    return answer

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))

    """
    制限時間オーバー
    """