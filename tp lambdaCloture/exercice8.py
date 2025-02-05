# Question 3
print("Question 3")

def calculerRemise(liste_prix, fonction_remise):
    """
    liste_prix : liste de prix [p1, p2, p3, ...]
    fonction_remise : fonction prenant un prix et retournant le prix après remise
    """
    prix_remises = [fonction_remise(prix) for prix in liste_prix]
    return sum(prix_remises)

# Question 4
print("Question 4")

produits = [100, 50, 300, 80]  # Exemple de prix
remise_20_pourcent = lambda p: p * 0.8  # applique 20 % de réduction

total_apres_remise = calculerRemise(produits, remise_20_pourcent)
print(total_apres_remise)
# Pour [100, 50, 300, 80], la somme est 530.
# Après -20%, on obtient 0.8 * 530 = 424
