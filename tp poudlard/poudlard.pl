% Déclaration des suspects
suspect(drago).
suspect(neville).
suspect(ginny).

% Déclaration des affirmations des suspects
declaration(drago, (coupable(drago) -> innocent(neville))).
declaration(neville, (coupable(drago) -> innocent(ginny))).
declaration(ginny, (coupable(ginny) -> (innocent(drago), innocent(neville)))).

% Une personne est innocente si elle n'est pas coupable
innocent(X) :- \+ coupable(X).

% Règles pour déterminer qui est coupable
coupable(drago) :- \+ innocent(drago), innocent(neville), innocent(ginny).
coupable(neville) :- \+ innocent(neville), innocent(drago), innocent(ginny).
coupable(ginny) :- \+ innocent(ginny), innocent(drago), innocent(neville).

% Définition de la règle pour déterminer qu'une seule personne est coupable parmi les suspects
unique_coupable([X, Y, Z]) :-
    coupable(X), innocent(Y), innocent(Z);
    innocent(X), coupable(Y), innocent(Z);
    innocent(X), innocent(Y), coupable(Z).

% Résolution pour déterminer qui est coupable
trouver_coupable(Coupable) :-
    unique_coupable([drago, neville, ginny]),
    coupable(Coupable).

% Ya rien qui marche j en ai marre