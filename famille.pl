% Base de connaissances initiale
homme(pierre).
homme(marc).
homme(paul).
homme(jacques).

femme(marie).
femme(sophie).
femme(julie).

% Relations parentales de base
parent(pierre, paul).
parent(marie, paul).
parent(marc, sophie).
parent(jacques, marc).
parent(julie, sophie).
parent(jacques, pierre).

% Règles pour pere et mere
pere(X, Y) :- homme(X), parent(X, Y).
mere(X, Y) :- femme(X), parent(X, Y).

% Règle pour les grands-parents
grand_parent(X, Y) :- parent(X, Z), parent(Z, Y).

% Règle pour les frères et sœurs
frere_soeur(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Règle pour les oncles et tantes
oncle_tante(X, Y) :- parent(Z, Y), frere_soeur(X, Z).

% Règle pour calculer la longueur d une liste
longueur([], 0).
longueur([_|Queue], N) :- longueur(Queue, M), N is M + 1.

% Règles pour la manipulation des listes
membre(X, [X|_]).
membre(X, [_|Queue]) :- membre(X, Queue).

% Règle pour les cousins
cousin(X, Y) :- parent(Z, X), frere_soeur(Z, W), parent(W, Y).