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

Lista1=TransformaNPEmLista(csv_in_numpy)  ## ok 
#print(Lista1[0])

##    ListaPrimeiroUltimo recebe a Lista1 que é uma lista com 2 indice e 
###   troca o primeiro indice pelo segundo  
####  por exemplo dado uma lista de um unico indice  l =[[1,2],[3,4],[5,6]] 
##### essa função vai troca [2,1,4,3,6,5]


ListaPrimeiroUltimo=primeiroUltimo_UltimoPrimeiro(Lista1)
#print(ListaPrimeiroUltimo)



###  A função dividirListaInversa pega a ListaPrimeiroUltimo é uma lista de um indice 
####  e transforma em lista com 2 indice 
prontoParaColocaNoDic=dividirListaInversa(ListaPrimeiroUltimo)
#print(prontoParaColocaNoDic)

dic1=retornaVerticeAdj(Lista1)
### ordenar lista é uma fnção que pega uma lista e organizar 
#### a forma de ordenção e que  o indice [i][0] é como se fosse a chave 
##### e o indice [i][j] sera o valor da chave 
###### loga os elementos da lista que tiverem a chave menor ficaram na frente 
lopp=ordenarLista(prontoParaColocaNoDic)

### aqui pega os elemenntos que tem o indice [i][0] igual e coloca  esse indice[i][0]  e criar uma chave
#### todos os elementos que tiveram o msm  indice [i][0] serão atribuidos a uma chave 
dic2=retornaVerticeAdj(lopp)



print("\n")
pprint(dic2)
print(dic2.get('999'))   ### não imprimiu todos 