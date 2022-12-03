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
  return ListaInverso


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

