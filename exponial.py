def pow_mod(n, k, m):
    ans = 1
    while k:
        if k & 1:
            ans = (ans * n) % m
        k //= 2
        n = (n * n) % m
    return ans

def phi(n):
    tot = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            tot *= i - 1
            n //= i
            while n % i == 0:
                tot *= i
                n //= i
        i += 1
    if n > 1:
        tot *= n - 1
    return tot

def solve(n, m):
    if m == 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return pow_mod(2, 1, m)
    if n == 3:
        return pow_mod(3, 2, m)
    if n == 4:
        return pow_mod(4, 9, m)
    tot_m = phi(m)
    return pow_mod(n, tot_m + solve(n - 1, tot_m), m)

n, m = map(int, input().split())
print(solve(n, m))
