n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

slovar_a, slovar_b = {}, {}
for i in range(n):
    if a[i] not in slovar_a:
        slovar_a[a[i]] = 0
    slovar_a[a[i]] += 1
    if b[i] not in slovar_b:
        slovar_b[b[i]] = 0
    slovar_b[b[i]] += 1

    print(b[i], end=' ')
    if slovar_a == slovar_b and i != n - 1:
        slovar_a.clear()
        slovar_b.clear()
        print('#', end=' ')