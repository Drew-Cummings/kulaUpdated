# this function handles error catching with the eval function
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
    print(type(sample[2][2]))
    print(sample[2][2])
    print(sample)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
