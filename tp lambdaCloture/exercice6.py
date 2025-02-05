# Question 1
print("Question 1")

def filtrerMapper(filtre, transformation, elements):
    # On filtre d’abord
    elements_filtres = filter(filtre, elements)
    # Puis on applique la transformation
    elements_transformes = map(transformation, elements_filtres)
    # On retourne la liste finale
    return list(elements_transformes)

# Question 2
print("Question 2")

chaines_exemple = ["hello", "", "world", "python", "", "lambda"]

resultat = filtrerMapper(
    lambda s: s != "",   # garde uniquement les chaînes non vides
    lambda s: s.upper(), # convertit la chaîne en majuscules
    chaines_exemple
)
print(resultat)
# Résultat attendu : ["HELLO", "WORLD", "PYTHON", "LAMBDA"]
