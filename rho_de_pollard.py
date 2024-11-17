import sys
import time
from fonction_principale import int_factor
from sieves import sieve

#On ajuste la limite de la taille des entiers convertis en chaîne
sys.set_int_max_str_digits(10**9)  # Par exemple, on permet des entiers avec jusqu'à 1 000 000 000 chiffres

primes = sieve(100000) #on fait appel à la fonction avec pour argument de calculer jusqu'aux 1000 premiers nombres premiers

#On entre ici le nombre que l'on veut factoriser et on lance le chrono
now = time.time()
nombre = 2**3400000-1
print(f"Longueur du nombre {len(str(nombre))}")
result = int_factor(nombre)
print(f"Décomposition de {nombre} en facteurs premiers :", result, f"en {time.time() - now} seconde(s)")