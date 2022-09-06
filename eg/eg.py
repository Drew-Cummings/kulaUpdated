from Types import *

def o(t):
    if type(t) is dict:
        for keys, values in t.items():
            print(values)
            
            if "^_" not in keys:
                values = o(values)
                t = 0
                for i in keys:
                    print(i)
            
            u = {}
            u[1+len(u)] = values
            
        #if len(t) == 0:
        output = ""
        for key, value in u:
            output += value + " "
    
    return output

def oo(t):
    print(o(t))
    return t

#test case
def the(t):
    oo(t)
    return True

def sym():
    sym = Types.Sym()
    pairs = ["a","a","a","a","b","b","c"]
    for i in pairs:
        sym.add(i)
    mode = sym.mid()
    entropy = sym.div()
    entropy = (1000*entropy)//1/1000
    oo({mode, entropy})
    if (mode == "a") and (entropy>=1.37) and (entropy<=1.38):
        return True
    else:
        return False

def num():
    num = Types.Num
    for i in range(1,100):
        num.add(i)
    mid = num.mid()
    div = num.div()
    print(mid, div)
    if (mid>=50) and (mid<=50) and (div>30.5) and (div<30):
        return True
    else:
        return False

def bignum():
    num = Types.Num
    nums = 32
    for i in range(1, 1000):
        num.add(i)
    oo(num.nums())
    if len(num) == 32:
        return True
    else:
        return False

