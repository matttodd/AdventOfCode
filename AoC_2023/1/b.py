
def main():
    print(solve())


def solve():
    ct = 0
    one = "one"
    two = "two"
    three = "three"
    four = "four"
    five = "five"
    six = "six"
    seven = "seven"
    eight = "eight"
    nine = "nine"
    num_to_digit = {one: "1", two: "2", three: "3", four: "4", five: "5", six: "6", seven: "7", eight: "8", nine: "9"}

    while True:
        try:
            next = input()
        except EOFError:
            return ct
        num = ""
        first_num_ind = 1000000000
        first_num_val = ""
        last_num_ind = 10000000000
        last_num_val = ""
        for number in num_to_digit.keys():
            if number in next:
                print(number)
                if next.index(number) < first_num_ind:
                    first_num_ind = next.index(number)
                    first_num_val = num_to_digit[number]
                if (''.join(reversed(next))).index(''.join(reversed(number))) < last_num_ind:
                    # print(''.join(reversed(next)), (''.join(reversed(number))), str(reversed(next)).index(str(reversed(number))), number)
                    last_num_ind = ''.join(reversed(next)).index(''.join(reversed(number)))
                    last_num_val = num_to_digit[number]
        for ind, i in enumerate(next):
            if i.isdigit():
                if ind < first_num_ind:
                    num += i
                else:
                    num += first_num_val
                break
        if len(num) == 0:
            num += first_num_val
        # print(num)
        for ind, i in enumerate(reversed(next)):
            if i.isdigit():
                if ind < last_num_ind:
                    num += i
                else:
                    num += last_num_val
                    # print(ind, len(next) - ind - 1, last_num_ind, last_num_val)
                break
        if len(num) == 1:
            num += last_num_val
        print(num)
        ct += int(num)



main()
