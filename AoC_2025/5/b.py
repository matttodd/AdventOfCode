import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from AoC_2025.utils.read import *

def solve(contents):
    fresh = []
    new_fresh = []
    ans = 0
    for content in contents:
        if content == "":
            break
        start, end = content.split("-")
        fresh.append((int(start), int(end)))
    fresh.sort()
    new_fresh.append(fresh[0])
    for f in fresh[1:]:
        prev = new_fresh[-1]
        if f[0] <= prev[1]: # overlap
            if f[1] <= prev[1]:
                continue
            new = (prev[0], f[1])
            new_fresh[-1] = new
        else:
            new_fresh.append(f)
    # print(fresh)
    # print(new_fresh)
    for f in new_fresh:
        ans += (f[1] - f[0]) + 1

    return str(ans)

def setup():
    contents = read_in()
    ans = solve(contents)
    write_out(ans)
    print(ans)

setup()