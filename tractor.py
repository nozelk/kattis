st_testnih_primerov = int(input())

for i in range(st_testnih_primerov):

    A, B = input().split()
    A = int(A)
    B = int(B)

    dostopni_kvadrati = 0

    premik = 0

    while True:

        dolzina_premika = 2 ** premik

        odstej_x = max(0, dolzina_premika - A - 1)

        odstej_y = max(0, dolzina_premika - B - 1)

        if dolzina_premika - odstej_x - odstej_y <= 0:
            break

        dostopni_kvadrati += dolzina_premika - odstej_x - odstej_y

        premik += 1

    print(dostopni_kvadrati)
