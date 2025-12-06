from pathlib import Path
import sys

def read_in(dont_strip = False):
    filename = "in.txt"
    caller = Path.cwd()
    full_path = caller / filename
    with open(full_path, "r") as file:
        if dont_strip:
            content = file.readlines()
        else:
            content = list(map(lambda x: x.strip(), file.readlines()))
    return content


def write_out(content):
    name = sys.argv[0].split(".")[0]
    filename = f"out_{name}.txt"
    caller = Path.cwd()
    full_path = caller / filename
    with open(full_path, "w") as file:
        file.write(content)