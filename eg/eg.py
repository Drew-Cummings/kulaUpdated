from Types import *
from Configs.config import *


def o(t):
    if type(t) is dict:
        u = {}
        for keys, values in t.items():
            # print(values)
            keys = str(keys)
            curr_pattern = re.compile("^_")
            # not starting with "_"
            # "help" is valid while "_help" isn't
            if len(re.findall(curr_pattern, keys)) == 0:
                values = o(values)
                # for i in keys:
                #     print(i)
            
            u[1+len(u)] = values
            
        # if len(t) == 0:
        output = "{"
        for key, value in u.items():
            output += str(value) + " "
        output += "}"
        print(output)
        return output
    else:
        return str(t)


def oo(t):
    print(o(t))
    return t


# test case
def the(t):
    oo(t)
    return True


def sym():
    test_sym = Types.sym.Sym(0, "test_sym")
    pairs = ["a", "a", "a", "a", "b", "b", "c"]
    for i in pairs:
        test_sym.add(i)
    mode = test_sym.mid(1)
    entropy = test_sym.div()
    entropy = (1000*entropy)//1/1000
    oo({mode, entropy})
    if (mode == "a") and (entropy >= 1.37) and (entropy <= 1.38):
        return True
    else:
        return False


def num():
    test_num = Types.num.Num(0, "test_num", 100)
    for i in range(1, 100):
        test_num.add(i)
    mid = test_num.mid()
    # TODO num.div? or dev?
    div = test_num.dev()
    print(mid, div)
    if (mid >= 50) and (mid <= 50) and (div > 30.5) and (div < 30):
        return True
    else:
        return False


def bignum():
    test_num = Types.num.Num(0, "test_bignum", 512)
    nums = 32
    for i in range(1, 1000):
        test_num.add(i)
    oo(test_num.nums())
    if len(test_num.numbers) == 32:
        return True
    else:
        return False
