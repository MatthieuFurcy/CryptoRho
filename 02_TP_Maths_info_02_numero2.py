import time as t

now = t.time()

def int_factor(n: int) -> dict:
    factor_prime = {}

    div = 2
    while n>1:  
        while n%div == 0:
            if div in factor_prime:
                factor_prime[div] += 1
            else:
                factor_prime[div] = 1
            n //= div
        div += 1
    return factor_prime

number = 345002232330002
result = int_factor(number)
print(f"Décomposition de {number} en facteurs premiers : {result} en {t.time() - now} seconde(s)")
