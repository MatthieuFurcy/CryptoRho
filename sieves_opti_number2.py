def sieve(limit):
    """
    Génère tous les nombres premiers jusqu'à la limite spécifiée en utilisant l'algorithme du crible d'Ératosthène.
    
    Args:
        limit (int): La limite supérieure jusqu'à laquelle trouver les nombres premiers.
        
    Returns:
        list: Une liste de nombres premiers jusqu'à la limite spécifiée.
    """
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [num for num, prime in enumerate(is_prime) if prime]

def primes(limit=100000):
    """
    Retourne une liste des nombres premiers jusqu'à une certaine limite.
    
    Args:
        limit (int): La limite supérieure jusqu'à laquelle trouver les nombres premiers.
        
    Returns:
        list: Une liste des nombres premiers jusqu'à la limite.
    """
    return sieve(limit)
