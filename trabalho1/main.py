# importar as bibliotecas necessárias
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

Lista1=TransformaNPEmLista(csv_in_numpy)   
print(Lista1[0])    ## ['1','22']
print(Lista1[0][0]) ## 1
print(Lista1[0][1]) ## 22

## ListaPrimeiroUltimo recebe a Lista1 que é uma lista com 1 indice e 
### troca o primeiro indice pelo segundo  
#### por exemplo dado uma lista de um unico indice  l =[1,2,3,4] essa função vai troca 2,1,3,4

ListaPrimeiroUltimo=primeiroUltimo_UltimoPrimeiro(Lista1)
print(ListaPrimeiroUltimo) ## 22
print(">>",ListaPrimeiroUltimo[46821]) ## 1
print(">>",len(ListaPrimeiroUltimo)) ## 1


### dividir Lista Inversa ta errada 
prontoParaColocaNoDic=dividirListaInversa(ListaPrimeiroUltimo)

dic1=retornaVerticeAdj(Lista1)
print(prontoParaColocaNoDic[46821])
#dic2=retornaVerticeAdj(prontoParaColocaNoDic)