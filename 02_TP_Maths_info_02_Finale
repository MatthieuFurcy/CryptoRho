## Programmation autour des nombres premiers - décomposition en facteurs premiers // TP Susset/Noël CIEL-IR1
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
    # Vérification que l'entrée est un entier positif (on sait jamais :)
    assert isinstance(n, int) and n > 0, "L'entrée doit être un entier positif."

    # Cas trivial, les nombres <= 1 n'ont pas de facteurs premiers
    if n <= 1:
        return {}
    
    # Traiter les nombres pairs séparément pour avoir une réduction immédiate
    if n % 2 == 0:
        factors = {2: 0}  # Initialiser le dictionnaire des facteurs
        while n % 2 == 0:  # Diviser par 2 autant que possible
            factors[2] += 1  # Compter l'exposant du facteur 2
            n //= 2  # Réduire n
        return {**factors, **int_factor(n)}  # #Retourner les facteurs trouvés avec la factorisation du reste
    
    # Vérifier les petits facteurs jusqu'à 1000
    for i in range(2, min(n, 1000)):
        if n % i == 0:  # Si n est divisible par i
            factors = {i: 0}  # Initialiser le dictionnaire des facteurs pour i
            while n % i == 0:  # Diviser par i autant que possible
                factors[i] += 1  # Compter l'exposant de i
                n //= i  # Réduire n
            return {**factors, **int_factor(n)}  # Retourner les facteurs trouvés avec la factorisation du reste
            # c'est une approche qui gère les cas où n a de petits facteurs,
            # évitant les échecs pour de petits nombres comme 21 (j'ai eu le soucis sans cette approche).
    
    def gcd(a, b):
        """
        Calculer le plus grand commun diviseur de a et b en utilisant l'algorithme d'Euclide.

        Args:
            a (int): Premier entier.
            b (int): Deuxième entier.

        Returns:
            int: Le plus grand commun diviseur de a et b.
        """
        while b:  # Tant que b n'est pas zéro
            a, b = b, a % b  # Mettre à jour a et b
        return a  # Retourner le GCD

    def f(x):
        """
        Fonction polynomiale utilisée dans l'algorithme de Pollard's Rho.

        Args:
            x (int): Entier d'entrée.

        Returns:
            int: Résultat de la fonction polynomiale.
        """
        return (x * x + 1) % n  # Fonction polynomiale, permet d'explorer les espaces de facteurs

    # Initialisation des variables
    x, y, d = 2, 2, 1  # x et y sont utilisés pour itérer, d pour stocker le GCD
    iterations = 0  # Compteur d'itérations pour éviter les boucles infinies

    # Boucle principale pour trouver un facteur
    while d == 1:  # Continue tant que d est égal à 1
        x = f(x)  # Déplacer x à la valeur suivante dans la séquence
        y = f(f(y))  # Déplacer y à la valeur suivante dans la séquence (deux fois plus vite que x)
        d = gcd(abs(x - y), n)  # Calculer le pgcd de la différence
        iterations += 1  # Incrémenter le compteur d'itérations

        # Limiter les itérations pour éviter les boucles infinies
        if iterations > 100:  # Si trop d'itérations sans convergence
            return {n: 1}  # Retourner n comme facteur, signifiant qu'aucun facteur n'a été trouvé

    # Si d est égal à n, cela signifie que n est un nombre premier
    if d == n:
        return {n: 1}
    
    # Factoriser récursivement d et n // d
    factors_d = int_factor(d)  # Factoriser le facteur trouvé
    factors_n_d = int_factor(n // d)  # Factoriser le reste n // d
    
    # Combiner les facteurs
    for key in factors_n_d:
        if key in factors_d:  # Si le facteur existe déjà
            factors_d[key] += factors_n_d[key]  # Ajouter les exposants
        else:
            factors_d[key] = factors_n_d[key]  # Ajouter un nouveau facteur
    
    return factors_d  # Retourner le dictionnaire des facteurs

# Exemple d'utilisation
now = time.time()
nombre = 127_168_904_561_1179  # Test avec 127_168_904_561_1179
result = int_factor(nombre)  # Appeler la fonction de factorisation
print(f"Décomposition de {nombre} en facteurs premiers : {result} en {time.time() - now} seconde(s)")

# Assertions pour les tests
assert int_factor(1) == {}, "Le cas de test pour n=1 a échoué"  # Vérification pour 1
assert int_factor(2) == {2: 1}, "Le cas de test pour n=2 a échoué"  # Vérification pour 2
assert int_factor(44) == {2: 2, 11: 1}, "Le cas de test pour n=44 a échoué"  # Vérification pour 44
assert int_factor(127_168_904_561_1179) == {13: 1, 97: 1, 149: 1, 6768299611: 1}, "Le cas de test pour n=127.... a échoué" # Vérification pour 127......
