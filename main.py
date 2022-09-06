# this function handles error catching with the eval function
from eg.eg import *
def improved_eval(n):
    try:
        output = eval(n)
    except (NameError, SyntaxError):
        output = eval(repr(n))
    return output
# this function reads in a csv file, converts the strings to a relevant data type,
# and stores them in the relevant location in a 2d array


def csv(filename):
    file = open(filename, "r")
    file1 = file.readlines()
    input = [l.split(',') for l in '\n'.join(file1).split('\n\n')]
    output = [list(map(improved_eval, i)) for i in input]
    return output


if __name__ == '__main__':
    sample = csv('Files/auto93.csv')
    config_the = get_the(csv_help)
    config_the = cli(config_the)
    print(config_the)

    test_table = {1: "str1", 2: "st2", 3: {1: "nest_str1", 2: "nest_str2"}}
    the(test_table)
    the(config_the)

    # print(type(sample[2][2]))
    # print(sample[2][2])
    # print(sample)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
