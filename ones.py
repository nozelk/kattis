from sys import stdin

vrstice = stdin.readlines()

# Zanka se izvaja dokler imamo še števila
for stevilka in vrstice:
    # Vsako novo število posebej
    n = int(stevilka.strip())
    # Ostanek predstavlja ostanek in ga definiramo na 1
    stevilo = 1
    # Definiramo spremenljivko s katero bomo šteli nove enice
    stej = 1
    while stevilo % n != 0:
        stevilo = (stevilo * 10 + 1) % n
        stej += 1

    print(stej)