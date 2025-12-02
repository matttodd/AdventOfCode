

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
            print(files)
            for key, val in files.items():
                # print(key, sum(val))
                if sum(val) <= 100_000:
                    count += sum(val)
            return count
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
