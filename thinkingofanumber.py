import math

def najmanjsi_skupni_veckratnik(seznam):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return a * b // gcd(a, b)

    nsv = 1
    for stevilo in seznam:
        nsv = lcm(nsv, stevilo)

    return nsv


while True:
    n = int(input())
    if n == 0:
        break
    delitelji = []
    maksimum = []
    minimum = [0]
    for i in range(n):
        podatek = input()
        if 'divisible' in podatek:
            delitelji.append(int(podatek.split()[2]))
        if 'less' in podatek:
            maksimum.append(int(podatek.split()[2]))
        if 'greater' in podatek:
            minimum.append(int(podatek.split()[2]))
    if len(maksimum) == 0:
        print('infinite')
    else:
        min_value = max(minimum) + 1
        max_value = min(maksimum) - 1
        lcm_value = najmanjsi_skupni_veckratnik(delitelji)
        if min_value > max_value:
            print('none')
        else:
            resitev = []
            first_divisible = ((min_value - 1) // lcm_value + 1) * lcm_value
            for stevilo in range(first_divisible, max_value + 1, lcm_value):
                resitev.append(str(stevilo))
            if len(resitev) == 0:
                print('none')
            else:
                print(' '.join(resitev))