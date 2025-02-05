# Question 1.1
print("Question 1.1")

# Expression lambda pour calculer le carré d'un nombre
carre = lambda x: x ** 2

# Exemple d’utilisation
print(carre(5))  # Affiche 25

# Question 1.2
print("Question 1.2")

nombres = [1, 2, 3, 4, 5]
# On réutilise la fonction lambda "carre" définie plus haut
carres = list(map(carre, nombres))
print(carres)  # Affiche [1, 4, 9, 16, 25]

# Question 1.3
print("Question 1.3")

addition = lambda a, b: a + b

# Exemple d’utilisation
print(addition(10, 5))  # Affiche 15

# Question 1.4
print("Question 1.4")

from functools import reduce

nombres = [1, 2, 3, 4, 5]
somme_totale = reduce(addition, nombres)  # "addition" est la lambda définie ci-dessus
print(somme_totale)  # Affiche 15
