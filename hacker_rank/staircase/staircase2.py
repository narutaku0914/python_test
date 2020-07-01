import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    stair_list = []
    for i in range(1, n+1):
        stair_list.append("".join(["#" for j in range(i)]))
    
    return stair_list


if __name__ == '__main__':
    n = int(input())

    for i in staircase(n):
        print(i.rjust(n, ' '))
