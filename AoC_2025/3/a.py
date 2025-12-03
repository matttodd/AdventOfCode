import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from AoC_2025.utils.read import *

def solve(contents):
    ans = 0
    for content in contents:
        cells = list(map(lambda x: int(x), list(content)))
        first = max(cells[:-1])
        first_i = cells.index(first)
        other = max(cells[first_i+1:])
        tot = int(str(first) + str(other))
        ans += tot
    return str(ans)

def setup():
    contents = read_in()
    ans = solve(contents)
    write_out(ans)
    print(ans)

setup()