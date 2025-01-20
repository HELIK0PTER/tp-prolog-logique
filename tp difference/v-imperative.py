# 1. Définition du dictionnaire de recettes
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


# 2. Fonction pour trouver les recettes possibles
def trouver_recettes_possibles(ingredients_disponibles):
    recettes_possibles = []

    for nom_recette, ingredients in recettes.items():
       # Vérifie si tous les ingrédients obligatoires sont disponibles
       if all(ingredient in ingredients_disponibles for ingredient in ingredients['obligatoires']):
           recettes_possibles.append(nom_recette)

    return recettes_possibles


# Exécution des tests
if __name__ == "__main__":
    # Test 1 : Ingrédients pour sandwich et salade
    print("Test 1 : Ingrédients pour sandwich et salade")
    ingredients1 = ['Pain', 'Beurre', 'Jambon', 'Huile', 'Vinaigre', 'Concombre', 'Tomate', 'Laitue']
    print(f"Ingrédients disponibles : {ingredients1}")
    print(f"Recettes possibles : {trouver_recettes_possibles(ingredients1)}\n")

    # Test 2 : Ingrédients pour omelette
    print("Test 2 : Ingrédients pour omelette")
    ingredients2 = ['Oeufs', 'Sel', 'Poivre', 'Fromage', 'Herbes']
    print(f"Ingrédients disponibles : {ingredients2}")
    print(f"Recettes possibles : {trouver_recettes_possibles(ingredients2)}\n")

    # Test 3 : Ingrédients incomplets pour pizza
    print("Test 3 : Ingrédients incomplets pour pizza")
    ingredients3 = ['Farine', 'Eau', 'Sel', 'Tomate']
    print(f"Ingrédients disponibles : {ingredients3}")
    print(f"Recettes possibles : {trouver_recettes_possibles(ingredients3)}\n")