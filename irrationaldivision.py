s = input()
p,q = int(s.split(" ")[0]),int(s.split(" ")[1])
if p % 2 == 0:
    print(0)
elif p % 2 == 1 and q % 2 == 1:
    print(1)
elif q > p:
    print(2)
else:
    print(0)

