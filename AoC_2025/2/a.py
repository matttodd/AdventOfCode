import sys
import os
from operator import truediv

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from AoC_2025.utils.read import *

def solve(contents):
    ranges = contents[0].split(',')
    ranges = map(lambda x: x.split('-'), ranges)
    ans = 0
    for r in ranges:
        print(r)
        a = int(r[0])
        b = int(r[1])
        for i in range(a, b+1):
            s = str(i)
            if s[:len(s)//2] == s[len(s)//2:]:
                ans += i
            # for j in range(len(s)):
            #     for k in range(j + 1, len(s)):
            #         if s.count(s[j:k]) > 1:
            #             ans += 1
    return str(ans)

def is_valid(num):
    return True

def setup():
    contents = read_in()
    ans = solve(contents)
    write_out(ans)
    print(ans)

setup()