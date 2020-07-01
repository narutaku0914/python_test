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

# それぞれの要素の個数を辞書(dictのサブクラス)で返す
from collections import Counter 


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_dict = Counter(magazine)
    note_dict = Counter(note)
    if (magazine_dict & note_dict) == note_dict:    # 集合演算はsetかdictのみ
        answer = "Yes"
    else:
        answer = "No"

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