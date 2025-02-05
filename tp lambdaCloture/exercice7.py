# Question 1
print("Question 7.1")

def memoriser(fonction):
    cache = {}
    def fonction_memo(*args):
        if args in cache:
            return cache[args]
        resultat = fonction(*args)
        cache[args] = resultat
        return resultat
    return fonction_memo

# Question 2
print("Question 7.2")

import time

def factorielle(n):
    return 1 if n <= 1 else n * factorielle(n - 1)

def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

factorielle_memo = memoriser(factorielle)
fibonacci_memo = memoriser(fibonacci)

# Mesure de temps sur factorielle(30)
debut = time.time()
print(factorielle_memo(30))
fin = time.time()
print(f"Factorielle(30) calculée en {fin - debut} secondes (avec mémorisation).")

# Mesure de temps sur fibonacci(30)
debut = time.time()
print(fibonacci_memo(30))
fin = time.time()
print(f"Fibonacci(30) calculé en {fin - debut} secondes (avec mémorisation).")

# Deuxième appel, le résultat devrait venir directement du cache
debut = time.time()
print(fibonacci_memo(30))
fin = time.time()
print(f"Deuxième appel de Fibonacci(30) en {fin - debut} secondes (cache).")
