def je_ok(ime):
    if len(ime) < 5 or len(set(ime)) != len(ime):
        return False
    return True

def najkrajsa(imena):
    dol = min(len(ime) for ime in imena)
    return [ime for ime in imena if len(ime) == dol]


def bestic(imena):
    ok_imea = [ime for ime in imena if je_ok(ime)]
    if len(ok_imea) == 0:
        return "Neibb"
    najkrajsa_imena = najkrajsa(ok_imea)
    return sorted(najkrajsa_imena)[-1]

n = int(input())
imena = [input().strip() for _ in range(n)]
print(bestic(imena))