import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pprint import pprint
from pprint import pprint

from  funcoes import*
# estilo notebook
sns.set()
# url dos datasets
#url_path = 'https://raw.githubusercontent.com/reidnersousa/6semestre/Teoria-Grafos/GrafoExemplo.txt'
url_path = 'https://raw.githubusercontent.com/reidnersousa/6semestre/Teoria-Grafos/as_graph.txt'
# df recebe o arquivo e transforma em DataFrame
df = pd.read_csv(url_path , sep ='\t',names=["Teste1"])

csv_in_numpy = df['Teste1'].to_numpy()
#print(arrayDi)


## TransformaEmLista é uma função que recebe um array np 
###  transforma em uma lista  de 2 indice 

lista1=TransformaNPEmLista(csv_in_numpy)  ## ok 
#print("Lista1 ",lista1)


lista2=primeiroUltimo_UltimoPrimeiro(lista1)
#print("Lista2",lista2) ###  é a lista so que oposto por exemplo se a lista 1 tem [1,22] a  lista 2 sera [22,1]
lopp=ordenarLista(lista2)
### lopp pode ta errado
#print("lista2 Ordenado",lopp)



dic1=retornaVerticeAdj(lista1)
#print("Lista Adjacente1",dic1)



### aqui pega os elemenntos que tem o indice [i][0] igual e coloca  esse indice[i][0]  e criar uma chave
#### todos os elementos que tiveram o msm  indice [i][0] serão atribuidos a uma chave 
dic2=retornaVerticeAdj(lista2)
#print("Lista Adjacente2 ",dic2)

### verifica no dic1 e no dic2 quais as chaves são iguais 
verticeRepetidos=qver(dic1,dic2)
#print("vertice Repetios",verticeRepetidos)
### retorna todos o vertice que o grafo tem 
#### tamano disso e 32385 vertice

verticeSemRepeticao =todosOsVerticeSemRepeticao(dic1,dic2)
print("Vertice Sem repeticao",verticeSemRepeticao)

listaQueVaiDefenirOsVertice=(juntandoAsDuasLista(lista1,lista2))
#print(listaQueVaiDefenirOsVertice)


print()
qVertice = numeroDeVertice(dic1,dic2)
print("Quantidade de vertice ",qVertice)

#grauDaListaAdjacente1=grauDeCadaVertice(dic1)
#print("grau da lista Adj1",grauDaListaAdjacente1)

#grauDaListaAdjacente2=grauDeCadaVertice(dic2)
#print("grau da lista Adj2",grauDaListaAdjacente2)