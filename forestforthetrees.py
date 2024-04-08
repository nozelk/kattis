from math import gcd

def v(trenuten_x, trenutn_y):
    if trenuten_x < x1 or trenuten_x > x2 or trenutn_y < y1 or trenutn_y > y2:
        return True
    return False

def resi(x, y, x1, x2, y1, y2):
    deljitel = gcd(x, y)

    if deljitel == 1:
        return "Yes"

    prvi_x = x // deljitel
    prvi_y = y // deljitel

    if v(prvi_x, prvi_y):
        return f"No\n{prvi_x} {prvi_y}"

    zac = 1
    konec = deljitel
    sredina = 0
    flag = False
    while zac < konec:
        sredina = (zac + konec) // 2
        if v(prvi_x * sredina, prvi_y * sredina):
            flag = True
            konec = sredina
        else:
            zac = sredina + 1
    if flag:
        return f"No\n{prvi_x * konec} {prvi_y * konec}"
    else:
        return "Yes"

x, y = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

print(resi(x, y, x1, x2, y1, y2))
