progenitor(maria, jose).
progenitor(joao, jose).
progenitor(joao, ana).
progenitor(jose, julia).
progenitor(jose, iris).
progenitor(iris, jorge).

mulher(maria).
mulher(ana).
mulher(julia).
mulher(iris).
homem(jose).
homem(joao).
homem(jorge).

prole(Y,X) :- progenitor(X,Y).
mae(X,Y) :- progenitor(X,Y), mae(X).
avos(X,Y):- progenitor(X,Y), mulher(X).
descendente(X,Z) :- progenitor(X,Z).
descendente(X,Z) :- progenitor(X,Z), descendente(Y,Z).
