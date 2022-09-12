import re
from Types.num import Num
from Types.sym import Sym


class Cols:

    def __init__(self, names):
        self.names = names
        self.all = []
        self.kclass = None
        self.x = {}
        self.y = {}
        num_pattern = re.compile("^[A-Z]*")
        skip_pattern = re.compile(":$")
        dependent_pattern = re.compile("[!+-]")
        single_dependent_pattern = re.compile("!$")
        for c, s in names.items():
            # Numbers start with uppercase letters
            if len(re.findall(num_pattern, s)) != 0:
                self.all.append(Num(c, s, 0))
            else:
                self.all.append(Sym(c, s))
            local_col = self.all[len(self.all) - 1]
            # for those columns' name which have a trailing + or -, we consider them as dependent variable
            if len(re.findall(skip_pattern, s)) == 0:
                if len(re.findall(dependent_pattern, s)) == 0:
                    self.x[c] = s
                else:
                    self.y[c] = s
                if len(re.findall(single_dependent_pattern, s)) != 0:
                    self.kclass = local_col
