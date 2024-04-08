import sys

# Branje vhodnih podatkov
n, m = sys.stdin.readline().split()
n = int(n)
m = int(m)
sosedje = {}
for i in range(1, n + 1):
    sosedje[i] = []

vhodne_vrstice = sys.stdin.readlines()
for vrstica in vhodne_vrstice:
    x, y = vrstica.split()
    x = int(x)
    y = int(y)
    sosedje[x].append(y)

# Iskanje unikatnih podgrafov
unikatni_podgrafi = set()
for vozlisce in range(1, n + 1):
    urejeni_sosedje = sorted(sosedje[vozlisce])
    podgraf_str = "-".join(str(sosed) for sosed in urejeni_sosedje)
    unikatni_podgrafi.add(podgraf_str)

# Izpis rezultata
print(len(unikatni_podgrafi))
