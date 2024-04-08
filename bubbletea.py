def najmanjsa_cena_toppinga(cena_gor,kombinacije):
    min_cena = float("inf")

    for i in kombinacije:
        min_cena = min(min_cena,cena_gor[i])
    return min_cena


st_cajov = int(input())
caji_cena = input()
caji_cena = [int(i) for i in caji_cena.split()]
stevilo_gor = int(input())
cena_gor = input()
cena_gor = [int(i) for i in cena_gor.split()]


for i in range(st_cajov):
    kombinacije = input()
    kombinacije = [int(i) - 1 for i in kombinacije.split()]
    kombinacije = kombinacije[1:]

    caji_cena[i] += najmanjsa_cena_toppinga(cena_gor,kombinacije)

denar = int(input())
najcanejsi = sorted(caji_cena)[0]
najvec_student = denar // najcanejsi - 1

if najvec_student <= 0:
    print(0)

else:
    print(najvec_student)