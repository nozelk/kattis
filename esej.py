def toword(n):
    temp = ""
    while n > 0:
        temp += chr(n % 26 + ord('a'))

        n //= 26
    return temp


n,m = input().split()
n = int(n)
m = int(m)



for i in range(1, m+1):
    print(toword(i), end=" ")
print()