import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    stair_list = []
    for i in range(1, n+1):
        stair_line_list = []
        stair_line_list.append("".join([" " for j in range(n-i)]))
        stair_line_list.append("".join(["#" for k in range(i)]))
        stair_list.append("".join(stair_line_list))
    
    return stair_list


if __name__ == '__main__':
    n = int(input())

    for i in staircase(n):
        print(i)
