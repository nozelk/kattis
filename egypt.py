slovar = {False : "wrong", True : "right"}

while True:
    
    a, b, c = map(int,input().split())
    tb = [a, b, c]
    tb.sort()
    if int(a) == 0 and int(b) == 0 and int(c) == 0:
        break

    print(slovar[(int(tb[0])**2 + int(tb[1])**2) == int(tb[2]) ** 2])