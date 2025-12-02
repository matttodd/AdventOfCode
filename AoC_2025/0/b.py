import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from AoC_2025.utils.read import *

def solve(contents):
    return str(0)

def setup():
    contents = read_in()
    ans = solve(contents)
    write_out(ans)
    print(ans)

setup()