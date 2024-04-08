import sys

def process_definition(d, v, s):
    if s[0] == 'def':
        if s[1] in d:
            del v[int(d[s[1]])]
        d[s[1]] = s[2]
        v[int(s[2])] = s[1]

def process_calculation(d, v, s):
    if len([z for z in s[1::2] if z in d]) != len(s[1::2]):
        print(" ".join(s[1:]), 'unknown')
    else:
        expression = " ".join([d[z] if z in d else z for z in s[1:-1]])
        val = eval(expression)
        if val in v:
            print(" ".join(s[1:]), v[val])
        else:
            print(" ".join(s[1:]), 'unknown')

def main():
    d = {}
    v = {}
    
    for line in sys.stdin:
        s = line.split()
        if s[0] == 'def':
            process_definition(d, v, s)
        elif s[0] == 'calc':
            process_calculation(d, v, s)
        else:
            d.clear()
            v.clear()

if __name__ == "__main__":
    main()
