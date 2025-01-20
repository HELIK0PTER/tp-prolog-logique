# 1. Définition du dictionnaire de recettes (même structure)
recettes = {
    'Pizza': {
       'obligatoires': ['Farine', 'Eau', 'Sel', 'Levure', 'Tomate', 'Fromage'],
       'optionnels': []
    },
    'Salade': {
       'obligatoires': ['Laitue', 'Tomate', 'Concombre', 'Vinaigre', 'Huile'],
       'optionnels': []
    },
    'Pates Carbonara': {
       'obligatoires': ['Pates', 'Creme', 'Lardons', 'Fromage', 'Sel', 'Poivre'],
       'optionnels': []
    },
    'Omelette': {
       'obligatoires': ['Oeufs', 'Sel', 'Poivre', 'Fromage'],
       'optionnels': ['Herbes']
    },
    'Sandwich': {
       'obligatoires': ['Pain', 'Beurre', 'Jambon'],
       'optionnels': ['Salade']
    }
}


# 2. Utilisation de filter et map pour trouver les recettes possibles
def trouver_recettes_possibles_func(ingredients_disponibles):
    # Fonction de filtrage qui vérifie si une recette est possible
    est_recette_possible = lambda recette: all(
       ingredient in ingredients_disponibles
       for ingredient in recette[1]['obligatoires']
    )

    # Filtrer les recettes possibles
    recettes_possibles = filter(est_recette_possible, recettes.items())

    # Transformer le résultat pour n'avoir que les noms des recettes
    return list(map(lambda x: x[0], recettes_possibles))


# Exécution des tests
if __name__ == "__main__":
    # Test avec différents ensembles d'ingrédients
    tests = [
       ['Pain', 'Beurre', 'Jambon', 'Huile', 'Vinaigre', 'Concombre', 'Tomate', 'Laitue'],
       ['Oeufs', 'Sel', 'Poivre', 'Fromage', 'Herbes'],
       ['Farine', 'Eau', 'Sel', 'Tomate']
    ]

    # Utiliser map pour formater l'affichage des résultats
    resultats = map(
       lambda ingredients: f"Avec {ingredients} on peut faire : {trouver_recettes_possibles_func(ingredients)}",
       tests
    )

    # Afficher les résultats
    print("\n".join(resultats))