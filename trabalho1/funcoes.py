from pprint import pprint
# importar as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pprint import pprint

import funcoes





######################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################
### função usando  na main primeira 
def TransformaNPEmLista(arrayDi):
    l=[]
    #Numero_de_linhas=46824
    
    ListaNP =list(arrayDi)
    ultimo=ListaNP[-1]                      ## 11616 29809
    ultimoIndex=ListaNP.index(ultimo)
    #print("ultimo elemento",ultimo,"p",ultimoIndex)
    Numero_de_linhas =int(ultimoIndex)+1    ##  ultimo Index = 46824 +1
    
    for i in range(1,Numero_de_linhas):
        #print(arrayDi[i])
        string = str(arrayDi[i])
        #print(string)
        lista = string.split()
        l.append(lista)
    return l



##################################################################################################################
##################################################################################################
##############################################################################################################################################################################################
    #### Criar uma tuple que armazena todos os valores de um indice  segunda 
    ### Função usando na main 
def retornaVerticeAdj(lista):
    
  vertice=lista[0][0] #1
  idx =0
  listaAux =[]
  dictonarioAux={}
  ultimaAresta=lista[-1][1]
  #print(ultimaAresta)
  while True:
    
    if vertice == lista[idx][0]:
      
      #print("entro no while")
      #print(lista[idx][0],":",lista[idx][1])
      listaAux.append(lista[idx][1])
    if vertice != lista[idx][0]:
      tuplaAux = tuple(listaAux)
      dictonarioAux.update({vertice: (tuplaAux)})

      #print(dictonarioAux.get('1'))

      #print(dictonarioAux.get('2'))
      #print("else",lista[idx][0],":",lista[idx][1])
    
      vertice = lista[idx][0]
      listaAux=[]
      tuplaAux=()
      idx -=1
      

    if lista[idx][1]==ultimaAresta:
      tuplaAux = tuple(listaAux)
      dictonarioAux.update({vertice: (tuplaAux)})

      #print(dictonarioAux.get('1'))

      #print(dictonarioAux.get('2'))
      #print("else",lista[idx][0],":",lista[idx][1])
    
      vertice = lista[idx][0]
      listaAux=[]
      tuplaAux=()
      idx -=1
      break
    
    idx += 1 

 
    
    
  return dictonarioAux


def primeiroUltimo_UltimoPrimeiro(ListaNP):
  listaAux=[]
  i = 0
  ultimo=ListaNP[-1]                      ## 11616 29809
  ultimoIndex=ListaNP.index(ultimo)
  #print(ultimoIndex)
  Numero_de_linhas =int(ultimoIndex)+1    ##  ultimo Index = 46824 +1
  #print(ListaNP[0])
  #print(ListaNP[-1])
  while i < Numero_de_linhas:
    #print(ListaNP[i][0],ListaNP[i][1])
    listaAux.append(ListaNP[i][1])
    listaAux.append(ListaNP[i][0])
    i += 1
  ListaInverso = listaAux
  return dividirListaInversa(ListaInverso)


def dividirListaInversa(lpu):
  listaParaDic=[]
  ue_lpu=lpu[-1]              #ultimo elemento de lpu
  iue_lpu=lpu.index(ue_lpu)    ## index do ultimo elememnto lpu
  #print(lpu[iue_lpu])
  indice =1
  ## tamanho 93643 93644 93645
  tamanho = len(lpu)
 # while indice != len(lpu):
  #  print(indice)
   # indice += 1
  #for indice in range (len(lpu)):
  for indice in range (0,len(lpu),2):
    juntando =''
    if indice % 2 ==0:
      idxPar=str(lpu[indice])
      #print(idxPar)
      #indice =+1
      indice +=1

      if indice % 2 != 0:
        
        
        idxImpar=str(lpu[indice])
        juntando = idxPar+' '+idxImpar
        stringCortadas = juntando.split()
        listaParaDic.append(stringCortadas)
  
  return listaParaDic




### demoras msms
def ordenarLista(olpcnd):
  lop=[]
  j=1
  for j in range (len(olpcnd)):
    for i in range (len(olpcnd)):
      if olpcnd[j][0] == olpcnd[i][0]:
        lop.append(olpcnd[i])        
  return lop



#  QuaisVerticeEstaoRepetidos?
### função que recebe o dic1:
######(que tem a chave que representa quais vertice estão conectados
##### e o valeus que repsenta quais vertice estão conectados

###### dic2 q(que tem a chave que repsenta quais vertice  e o values que 
#### repsenta quais vertice estão conectados )

def qver(d1,d2):

  
  chavesDic1 = tuple(d1.keys())
  chavesDic2 = tuple(d2.keys())
  verticeIguais=[]

  for i in range (len(chavesDic1)):
    for  j in range (len(chavesDic2)):
      if chavesDic1[i] in chavesDic2[j]:
        verticeIguais.append(chavesDic2[j])

  return verticeIguais
def elementosNaListaRepetidos(dados):
    
  valores = []
  repetidos = set() ## para coloca o elemento reptidos so uma vez 

  for dado in dados:
      if dado not in valores: 
        valores.append(dado)
      else:
        repetidos.add(dado)
  return valores

def numeroDeVertice(dic1,dic2):
  lista1Dic1 = dic1
  lista2Dic2 = dic2
  todosVertice =[y for x in [lista1Dic1,lista2Dic2] for y in x]
  qtdVertice =(elementosNaListaRepetidos(todosVertice))
  todosVerticeSemRepeticao =qtdVertice
  
 
  qtdVertice = list(qtdVertice)
  
  quantidadeDeVertice = len(qtdVertice)
  return quantidadeDeVertice


def todosOsVerticeSemRepeticao(dic1,dic2):
  lista1Dic1 = dic1
  lista2Dic2 = dic2
  todosVertice =[y for x in [lista1Dic1,lista2Dic2] for y in x]
  qtdVertice =(elementosNaListaRepetidos(todosVertice))
  todosVerticeSemRepeticao =qtdVertice
  
 
  qtdVertice = list(qtdVertice)
  
  quantidadeDeVertice = len(qtdVertice)
  return todosVerticeSemRepeticao

def juntandoAsDuasLista(lista1,lista1Oposta):
  lista1Dic1 = lista1
  lista2Dic2 = lista1Oposta
  listaPrincipal =[y for x in [lista1Dic1,lista2Dic2] for y in x]
  
  return listaPrincipal



def grauDeCadaVertice(listaAdj):
  ### grau de cada Vertice
  gdcVertice={}
  i=1
  ll=list(listaAdj.keys())
  tam = len(ll)
  print(tam)
  while True:
  #for i in range(1,7):
    p = str(i)
    g=listaAdj.get(p)
    #print("tamanho de g",g,"p",p)
    ow=len(g)

    #print(ow)
    #print("g",g,"\np",p)
    grauVertice = ow
    gdcVertice.update({p:(grauVertice)})
    
   
    if i == len(listaAdj.keys()):
      break
    i +=1
  return gdcVertice