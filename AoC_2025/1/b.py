import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
print(project_root)

from AoC_2025.utils.read import *

def solve(contents):
    pos = 50
    ans = 0
    for content in contents:
        dir = content[0]
        dist = int(content[1:])
        was_zero = pos == 0
        if dir == 'R':
            pos += dist
        else:
            pos -= dist
        if pos < 0 and was_zero:
            # from 0: -1 - -99 -> + 0: -100 - -199 -> + 1
            ans += abs((pos - 1) // 100) - 1
        elif pos < 0 and not was_zero:
            # from 5: -1 - -99 -> + 1: -100 - -199 -> + 2
            ans += abs((pos - 1) // 100)
        elif pos >= 100:
            ans += pos // 100
        elif pos == 0:
            ans += 1
        # print(dir, dist, pos, pos % 100, ans)
        pos = pos % 100
    return str(ans)

def setup():
    contents = read_in()
    ans = solve(contents)
    write_out(ans)
    print(ans)

setup()

