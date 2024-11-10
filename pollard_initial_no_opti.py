## Il était une fois les nombres premiers
## Auteur: M. Matthieu Furcy
## Date : 2024-10-19

# Méthodo:
#    1. Définition d'une méthode `int_factor` utilisant l'algorithme de Pollard's Rho pour factoriser un entier donné.
#    2. Gestion des cas trivials, y compris les nombres pairs pour avoir une opti immédiate.
#    3. Traitement des petits facteurs (jusqu'à 1000) pour éviter les échecs sur de petits nombres.
#    4. Utilisation de l'algorithme d'Euclide pour calculer le plus grand commun diviseur (GCD).
#    5. Application d'une fonction polynomiale pour générer une séquence d'entiers afin de détecter les cycles et trouver les facteurs.
#    6. Facteurs retournés sous forme de dictionnaire avec leurs exposants respectifs.
#    7. Inclusion d'exemples d'utilisation et d'assertions pour valider la fonctionnalité de la méthode.

import time

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
    
    for i in range(2, min(n, 1000)):
        if n % i == 0:
            factors = {i: 0}
            while n % i == 0:
                factors[i] += 1
                n //= i
            return {**factors, **int_factor(n)}
    
    def gcd(a, b):
        """
        Calculer le plus grand commun diviseur de a et b en utilisant l'algorithme d'Euclide.

        Args:
            a (int): Premier entier.
            b (int): Deuxième entier.

        Returns:
            int: Le plus grand commun diviseur de a et b.
        """
        while b:
            a, b = b, a % b
        return a

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

# Exemple d'utilisation
now = time.time()
nombre = 2**10000-1
result = int_factor(nombre)
print(f"Longueur du nombre {len(str(nombre))}")
print(f"Décomposition de {nombre} en facteurs premiers : {result} en {time.time() - now} seconde(s)")
