st_primerov = int(input())
for primer in range(st_primerov):
    st_vrstic = int(input())
    tabela_oseb = []
    for i in range(st_vrstic):
        vrstica = input().split()
        ime = vrstica[0].split(':')[0]
        razred = vrstica[1].split('-')
        razred.reverse()
        razred = [x.replace('lower','z') for x in razred] #z bo tako max tabela
        razred = [x.replace('upper','a') for x in razred] #a bo min tabele
        a = ['middle' for x in range(10)]
        a[0:len(razred)] = razred
        a.append(ime)
        tabela_oseb.append(a)
    tabela_oseb.sort()
    #print(tabela_oseb)
    for i in range(st_vrstic):
        print(tabela_oseb[i][10]) #izpiše imena, ki so 10-ti člen tabel
    print('=' * 30)