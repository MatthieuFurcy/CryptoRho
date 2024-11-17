import math
from sieves import sieve
from sieves import primes  # Assurez-vous que cette fonction génère une liste de nombres premiers.

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

    # Divise par 2 autant de fois que possible
    if n % 2 == 0:
        factors = {2: 0}
        while n % 2 == 0:
            factors[2] += 1
            n //= 2
        return {**factors, **int_factor(n)}

    # Appelle la fonction `primes` pour obtenir une liste de nombres premiers
    primes_list = primes()  # Assurez-vous que `10000` soit un argument valide pour générer suffisamment de nombres premiers

    # Boucle sur les nombres premiers générés par `primes_list`
    for i in primes_list:
        if n % i == 0:
            factors = {i: 0}
            while n % i == 0:
                factors[i] += 1
                n //= i
            return {**factors, **int_factor(n)}

    # Fonction gcd pour trouver le plus grand diviseur commun
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

    # Initialisation de l'algorithme de Pollard Rho
    x, y, d = 2, 2, 1
    iterations = 0

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
        iterations += 1

        if iterations > 20:
            return {n: 1}

    if d == n:
        return {n: 1}

    # Récursion pour les facteurs obtenus
    factors_d = int_factor(d)
    factors_n_d = int_factor(n // d)

    for key in factors_n_d:
        if key in factors_d:
            factors_d[key] += factors_n_d[key]
        else:
            factors_d[key] = factors_n_d[key]

    return factors_d
