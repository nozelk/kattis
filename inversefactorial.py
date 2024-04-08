mod = 10**9 + 7

s = input()

yet = 0
for c in s:
    yet = yet*10 + int(c)
    yet %= mod

here = 1
for i in range(1, mod+1):
    here = here * i % mod
    
    if here == yet:
        print(i)
        break
