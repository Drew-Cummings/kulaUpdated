from Types import *
from Configs.config import *
import random
import Types.data
from Types.csv import csv


# def runs(test_func_str):
class Eg:

    def __init__(self, test_config):
        """
        :param test_config: "the" config that get from the command line arguments
        """
        self.function_table = {"LIST": self.LIST,
                               # "BAD": self.BAD,
                               "ALL": self.ALL,
                               "LS": self.LS,
                               "the": self.the,
                               "sym": self.sym,
                               "num": self.num,
                               "bignum": self.bignum,
                               "csv": self.csv,
                               "data": self.data,
                               "stats": self.stats
                               }
        self.fails = 0
        self.test_config = test_config

    # o and oo are utility functions
    def o(self, t):
        if type(t) is dict:
            u = {}
            for keys, values in t.items():
                # print(values)
                keys = str(keys)
                curr_pattern = re.compile("^_")
                # not starting with "_"
                # "help" is valid while "_help" isn't
                if len(re.findall(curr_pattern, keys)) == 0:
                    values = self.o(values)
                    # for i in keys:
                    #     print(i)

                u[1 + len(u)] = values

            # if len(t) == 0:
            output = "{"
            for key, value in u.items():
                output += str(value) + " "
            output += "}"
            print(output)
            return output
        else:
            return str(t)

    def oo(self, t):
        print(self.o(t))
        return t

    # Test Engine
    def runs(self, test_str):
        if self.function_table.get(test_str) is None:
            return False
        # randomize the config variable's seed key
        random.seed(int(self.test_config["seed"]))
        old = {}
        for k, v in self.test_config.items():
            old[k] = v
        if self.test_config["dump"] == "True" or self.test_config["dump"] == "true":
            status, out = True, self.function_table[test_str]()
        else:
            try:
                status, out = True, self.function_table[test_str]()
            except Exception:
                status = False
                out = False
        for k, v in old.items():
            self.test_config[k] = v
        if status:
            if out:
                msg = "PASS"
            else:
                msg = "FAIL"
        else:
            msg = "CRASH"
        print("!!!!!!", msg, test_str, status)
        return out

    def BAD(self):
        raise ValueError("Intentionally crashing this!")

    def LIST(self):
        t = {}
        for k, v in self.function_table.items():
            t[k] = v
        return t

    def LS(self):
        print("\nExamples python csv -e ...")
        for n, f in self.LIST().items():
            print(f'\t{n}')
        return True

    def ALL(self):
        for n, f in self.LIST().items():
            if n != "ALL":
                print("\n-----------------------------------")
                if not self.runs(n):
                    self.fails += 1
        return self.fails

    # test case
    def the(self):
        self.oo(self.test_config)
        return True

    def sym(self):
        test_sym = Types.sym.Sym(0, "test_sym")
        pairs = ["a", "a", "a", "a", "b", "b", "c"]
        for i in pairs:
            test_sym.add(i)
        mode = test_sym.mid(1)
        entropy = test_sym.div()
        entropy = (1000 * entropy) // 1 / 1000
        self.oo({mode, entropy})
        if (mode == "a") and (entropy >= 1.37) and (entropy <= 1.38):
            return True
        else:
            return False

    def num(self):
        test_num = Types.num.Num(0, "test_num", 100)
        for i in range(1, 101):
            test_num.add(i)
        mid = test_num.mid()
        div = test_num.div()
        print(mid, div)
        if (mid >= 50) and (mid <= 52) and (div > 30.5) and (div < 32):
            return True
        else:
            return False

    def bignum(self):
        test_num = Types.num.Num(0, "test_bignum", 32)
        for i in range(1, 1000):
            test_num.add(i)
        self.oo(test_num.nums())
        if len(test_num.numbers) == 32:
            print(test_num.numbers)
            return True
        else:
            return False

    def csv(self):
        n = 0
        data = csv('Files/auto93.csv')
        for _ in data:
            n += 1
            if n > 10:
                return True
        return True

    def data(self):
        test_data = Types.data.Data("Files/auto93.csv")
        for x in test_data.cols.y:
            self.oo(x)
        return True

    def stats(self):
        test_data = Types.data.Data("Files/auto93.csv")

        def div(col):
            return col.div()

        def mid(col):
            return col.mid()

        print("xmid", self.o(test_data.stats(2, test_data.cols.x, 'mid')))
        print("xdiv", self.o(test_data.stats(3, test_data.cols.x, 'div')))
        print("ymid", self.o(test_data.stats(2, test_data.cols.y, 'mid')))
        print("ydiv", self.o(test_data.stats(3, test_data.cols.y, 'div')))

        return True
