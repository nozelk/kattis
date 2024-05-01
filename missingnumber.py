def najdi(s):
    for ind, st in enumerate(s):
        if int(st) != ind + 1:
            return ind + 1
        if ind + 1 == 9:
            break
    i = 9
    prev_st = 9
    try:
        while True:
            st = s[i] + s[i + 1]
            if int(st) - int(prev_st) != 1:
                return prev_st + 1
            i += 2
            prev_st = int(st)
    except IndexError:
        return n

n = int(input())
s = input()
print(najdi(s))
