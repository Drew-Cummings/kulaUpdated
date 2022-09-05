import re
import sys

csv_help = """CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD−2 license
USAGE: lua seen.lua [OPTIONS]
OPTIONS:
 -e --eg start−up example = nothing
 -d --dump on test failure, exit with stack dump = false
 -f --file file with csv data = ../data/auto93.csv
 -h --help show help = false
 -n --nums number of nums to keep = 512
 -s --seed random number seed = 10019
 -S --seperator feild seperator = , """


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def coerce(s):
    def fun(s1):
        if s1 == 'true':
            return True
        if s1 == 'false':
            return False
    if represents_int(s):
        return int(s)
    return fun(s.strip())


def get_the(config_help):
    the = {}
    pattern = re.compile(r"\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)")
    for (letters, numbers) in re.findall(pattern, config_help):
        the[letters] = numbers
        # print(letters, "  ", numbers)
    return the


def cli(the):
    for key, value in the.items():
        str_v = str(value)
        for n, x in zip(range(len(sys.argv)), sys.argv):
            if x == "-" + key[0] or x == "--" + key:
                str_v = sys.argv[n + 1]
        the[key] = str_v
    if "help" in the and the["help"] == "true":
        print(csv_help)
        exit(0)
    return the


# config_the = get_the(csv_help)
# config_the = cli(config_the)
# print(config_the)
# print(csv_help)