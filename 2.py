
import numpy as np


def is_safe(vals):
    if sorted(vals) != vals and sorted(vals, reverse=True) != vals:
        return False

    def diff_ok(v):
        for i in range(1,len(v)):
            if 1 <= abs(v[i]-v[i-1]) <= 3:
                continue
            else:
                return False
        return True
    
    if not diff_ok(vals):
        return False
    
    return True

def p1(lines):
    out = 0
    for l in lines:
        vals = [int(x) for x in l.split()]
        if is_safe(vals):
            out+=1

    return out


def p2(lines):
    out = 0
    for l in lines:
        vals = [int(x) for x in l.split()]
        if is_safe(vals):
            out+=1
        else:
            for i in range(len(vals)):
                vtest = vals[:i] + vals[i+1:]
                if is_safe(vtest):
                    out+=1
                    break
            
    
    return out



if __name__ == "__main__":
    with open("inputs/2.txt", "r+") as f:
        lines = f.readlines()
    
    print(p1(lines))
    print(p2(lines))