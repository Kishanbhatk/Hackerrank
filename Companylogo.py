#!/bin/python3
from collections import Counter

if __name__ == '__main__':
 str = sorted(list(input().strip()))
 d = list(Counter(str).items())
 l = sorted(d,key = lambda x : (x[1] * -1,x[0]))
 for i in range(0,3):
    print(l[i][0],l[i][1])
