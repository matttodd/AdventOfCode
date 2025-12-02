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
        if dir == 'R':
            pos += dist
        else:
            pos -= dist
        pos = pos % 100
        if pos == 0:
            ans += 1
    return str(ans)

def setup():
    contents = read_in()
    ans = solve(contents)
    write_out(ans)
    print(ans)

setup()

