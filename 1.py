
from collections import Counter


def p1(lines):
    l = []
    r = []
    for line in lines:
        left, right = line.split()
        l.append(int(left))
        r.append(int(right))
    
    out = 0
    for a,b in zip(sorted(l), sorted(r)):
        out += abs(a-b)
    return out

def p2(lines):
    l = []
    r = []
    for line in lines:
        left, right = line.split()
        l.append(int(left))
        r.append(int(right))
    
    l = set(l)
    out = 0
    for k,v in Counter(r).items():
        if k in l:
            out += k*v
    return out
    

if __name__ == "__main__":
    with open("inputs/1.txt", "r+") as f:
        lines = f.readlines()
    
    print(p1(lines))
    print(p2(lines))