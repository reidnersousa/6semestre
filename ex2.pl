
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

sexo(maria,feminino).
sexo(ana,feminino).
sexo(julia,feminino).
sexo(iris,feminino).
sexo(jose,masculino).
sexo(joao,masculino).
sexo(jorge,masculino).
homem(jose).
homem(joao).
homem(jorge).



%% X é o pai/mae e Y é o filho/filha
pai(X,Y) :- progenitor(X,Y),sexo(X,masculino).
mae(X,Y) :- progenitor(X,Y),sexo(X,feminino).
pais(X,Y):-progenitor(X,Y).
filho(Y,X) :- progenitor(X,Y),sexo(Y,masculino).
filha(Y,X) :- progenitor(X,Y),sexo(Y,feminino).
filho_a_(Y,X):-progenitor(X,Y).

%%% X irma e Y é´o irmao 
irma(X,Y):-progenitor(A,X),progenitor(A,Y),X\==Y , sexo(X,feminino).
%% X irmao e Y é irma
irmao(X,Y):-progenitor(A,X),progenitor(A,Y),X\==Y , sexo(X,masculino).

descendente(X,Y):-progenitor(X,Y).
%descendente(X,Y):-progenitor(X,Y),descendente(A,Y).


vô(X,Y):-progenitor(X,A),progenitor(A,Y),sexo(X,masculino).
vó(X,Y):-progenitor(X,A),progenitor(A,Y),sexo(X,feminino).
avós(X,Y):-progenitor(X,A),progenitor(A,Y).
avós_paternos(X,Y):-progenitor(X,A),sexo(A,masculino),progenitor(A,Y).
avós_maternos(X,Y):-progenitor(X,A),sexo(A,feminino),progenitor(A,Y).

%% consulta que mostrar os netos 
neto/a(X,Y):-filho_a_(X,A),filho_a_(A,Y).


%% X é o tio/tia e Y e o sobrinho logo
tio(X,Y):-irmao(X,A),progenitor(A,Y).
tia(X,Y):-irma(X,A),progenitor(A,Y).

%% X é o sobrinho e  Y é a tia  
sobrinho(X,Y):-irma(Y,A),filho(X,A).

sobrinha(X,Y):-irma(Y,A),filha(X,A).

%%% X é  ascendente  e Y é os pais 
ascendente(X,Y):-filho_a_(X,Y).






