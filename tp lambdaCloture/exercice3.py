# Question 3.1
print("Question 3.1")

mots = ["pomme", "avion", "chat", "ballon", "amour", "parapluie"]

# Question 3.2
print("Question 3.2")

mots_commencent_par_a = list(filter(lambda mot: mot.startswith("a"), mots))
print(mots_commencent_par_a)
# Par exemple, ["avion", "amour"]

# Question 3.3
print("Question 3.3")

def creer_compteur_longueur(min_longueur):
    compteur = 0
    def compteur_de_mots(liste_mots):
        nonlocal compteur
        compteur = sum(1 for m in liste_mots if len(m) > min_longueur)
        return compteur
    return compteur_de_mots

compteur_longueur_5 = creer_compteur_longueur(5)
nombre_mots_longs = compteur_longueur_5(mots)
print(nombre_mots_longs)  # Affiche le nombre de mots ayant plus de 5 caractères

