import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from AoC_2025.utils.read import *

def solve(contents):
    ans = 0
    for content in contents:
        cells = list(map(lambda x: int(x), list(content)))
        cur = ""
        pointer = 0
        for i in range(11, -1, -1):
            # print(cur, pointer, i, cells[pointer:-i])
            to_consider = cells[pointer:] if i == 0 else cells[pointer:-i]
            first = max(to_consider)
            pointer += cells[pointer:].index(first) + 1
            cur += str(first)
        ans += int(cur)
    return str(ans)

def setup():
    contents = read_in()
    ans = solve(contents)
    write_out(ans)
    print(ans)

setup()