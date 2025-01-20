ingredient_recette(pizza, farine).
ingredient_recette(pizza, eau).
ingredient_recette(pizza, sel).
ingredient_recette(pizza, levure).
ingredient_recette(pizza, tomate).
ingredient_recette(pizza, fromage).

ingredient_recette(salade, laitue).
ingredient_recette(salade, tomate).
ingredient_recette(salade, concombre).
ingredient_recette(salade, vinaigre).
ingredient_recette(salade, huile).

ingredient_recette(pates_carbonara, pates).
ingredient_recette(pates_carbonara, creme).
ingredient_recette(pates_carbonara, lardons).
ingredient_recette(pates_carbonara, fromage).
ingredient_recette(pates_carbonara, sel).
ingredient_recette(pates_carbonara, poivre).

ingredient_recette(omelette, oeufs).
ingredient_recette(omelette, sel).
ingredient_recette(omelette, poivre).
ingredient_recette(omelette, fromage).

ingredient_recette(sandwich, pain).
ingredient_recette(sandwich, beurre).
ingredient_recette(sandwich, jambon).

ingredient_optionnel(omelette, herbes).
ingredient_optionnel(sandwich, salade).

recette_possible(Recette, IngredientsDisponibles) :-
    distinct(Recette, (
        ingredient_recette(Recette, _),
        findall(I, ingredient_recette(Recette, I), IngredientsNecessaires),
        subset(IngredientsNecessaires, IngredientsDisponibles)
    )).
