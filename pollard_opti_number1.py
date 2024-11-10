## Il était une fois les nombres premiers
## Auteurs: M. Matthieu Furcy et M.Chamesddine Cloarec
## Date : 2024-11-10


#On importe les librairies nécessaires à notre programme
import sys
import time
import math

#On ajuste la limite de la taille des entiers convertis en chaîne
sys.set_int_max_str_digits(10**9)  # Par exemple, on permet des entiers avec jusqu'à 1 000 000 000 chiffres

#On utilise le cribble d'ératostène pour calculer efficacement les petits nombres premiers
def sieve(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return primes

primes = sieve(1000) #on fait appel à la fonction avec pour argument de calculer jusqu'aux 1000 premiers nombres premiers

#On définit une fonction int_factor qui va basiquement contenir nos calculs pour appliquer l'algorithme de Rho de Pollard
def int_factor(n: int) -> dict:
    """
    Effectue l'algorithme de Pollard's Rho pour factoriser un entier donné n.

    Args:
        n (int): L'entier à factoriser.

    Returns:
        dict: Un dictionnaire où les clés sont les facteurs premiers et les valeurs sont leurs exposants respectifs.
    """
    assert isinstance(n, int) and n > 0, "L'entrée doit être un entier positif."

    if n <= 1:
        return {}

    if n % 2 == 0:
        factors = {2: 0}
        while n % 2 == 0:
            factors[2] += 1
            n //= 2
        return {**factors, **int_factor(n)}

    for i in primes:
        if n % i == 0:
            factors = {i: 0}
            while n % i == 0:
                factors[i] += 1
                n //= i
            return {**factors, **int_factor(n)}
        
    '''
    On défini ici une fonction très importante en appelant 
    la fonction gcd de la librairie math précédemment importée,
    cette fonction va nous permettre de trouver le plus grand diviseur commun
    celle de math est extrêmement optimisée et écrite en C
    '''
    def gcd(a, b):
        return math.gcd(a, b)

    def f(x):
        """
        Fonction polynomiale utilisée dans l'algorithme de Pollard's Rho.

        Args:
            x (int): Entier d'entrée.

        Returns:
            int: Résultat de la fonction polynomiale.
        """
        return (x * x + 1) % n

    x, y, d = 2, 2, 1
    iterations = 0

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
        iterations += 1

        if iterations > 100:
            return {n: 1}

    if d == n:
        return {n: 1}

    factors_d = int_factor(d)
    factors_n_d = int_factor(n // d)

    for key in factors_n_d:
        if key in factors_d:
            factors_d[key] += factors_n_d[key]
        else:
            factors_d[key] = factors_n_d[key]

    return factors_d

#On entre ici le nombre que l'on veut factoriser et on lance le chrono
now = time.time()
nombre = 15**500000-1
result = int_factor(nombre)
print(f"Longueur du nombre {len(str(nombre))}")
print(f"Décomposition de {nombre} en facteurs premiers :", result, f"en {time.time() - now} seconde(s)")
