import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from AoC_2025.utils.read import *

def solve(contents):
    pt2 = False
    fresh = []
    ans = 0
    for content in contents:
        if content == "":
            pt2 = True
            continue
        if not pt2:
            start, end = content.split("-")
            fresh.append(range(int(start), int(end) + 1))
        else:
            i = int(content)
            for f in fresh:
                ans += 1 if i in f else 0
                if i in f:
                    break

    return str(ans)

def setup():
    contents = read_in()
    ans = solve(contents)
    write_out(ans)
    print(ans)

setup()