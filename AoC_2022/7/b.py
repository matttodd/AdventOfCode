MAX = 70000000
NEEDED = 30000000


def main():
    print(solve())


def solve():
    files = {}
    parents = []
    most_recent = None
    count = 0
    while True:
        try:
            inp = input().split()
        except EOFError:
            total = sum(files["/"])
            needed_to_free = total - (MAX - NEEDED)
            curr = None
            diff = MAX
            print(total, needed_to_free)
            for key, val in files.items():
                if sum(val) >= needed_to_free and sum(val) - needed_to_free < diff:
                    print(key, sum(val))
                    diff = sum(val) - needed_to_free
                    curr = key
            print(files[curr], sum(files[curr]), diff)
            return curr
        if (inp[0] == "$") and (inp[1] == "cd"):
            if inp[2] == "..":
                parents.pop()
            else:
                # Do Command
                while inp[2] in files:
                    inp[2] = inp[2] + "_"
                most_recent = inp[2]
                parents.append(most_recent)
                files[inp[2]] = []
        else:
            try:
                size = int(inp[0])
                for parent in parents:
                    files[parent].append(size)
            except ValueError:
                continue


main()
