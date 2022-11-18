from pprint import pprint
# importar as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pprint import pprint

import funcoes


def CriarRotas(verticeInicial,verticeFinal):
  rotas =[]
  numerosAresta =5 # criar uma função que calcular o numero de aresta 
  i=0
  while i<numerosAresta:
    
    aux=[(verticeInicial[i],verticeFinal[i])]
    rotas.append(aux)
    i +=1 

  return rotas



######################################################################################################################################################################################################
#################################################################################################################################################################################################################
#################################################

def TransformaNPEmLista(arrayDi):
    l=[]
    Numero_de_linhas=46824
    
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
    #### Criar uma tuple que armazena todos os valores de um indice 
def retornaVerticeAdj(lista):
    
  vertice=lista[0][0] #1
  idx =0
  listaAux =[]
  dictonarioAux={}
  
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
      

    if lista[idx][1]=='29809':
      print("AAA")
      break
    
    idx += 1 

 
    
    
  return dictonarioAux


#################################################################################################################################################################
#####################################################################################################################################################
# criando uma função que recebe ArrayDi e dividir em dois 
# essa função serve como auxiliar para a  função que vai criar a lista
def SeperandoArrayDi(arrayDi):
  i=1
  j=1
  
  VerticeInicial =[]
  VerticeFinal =[]
  tam =int(NumeroDeNo(arrayDi))
  print(tam)
  while i<tam:
    aux =int(arrayDi[i][0])
    VerticeInicial.append(aux) # convert str em int 
    #VerticeInicial.append(arrayDi[i][0])
    i +=1
    if arrayDi[tam][0]==arrayDi[i][0]:
      aux =int(arrayDi[i][0])
      VerticeInicial.append(aux)
      #VerticeInicial.append(arrayDi[i][0])
  while j <5:

    auj =int(arrayDi[j][2])
    VerticeFinal.append(auj)
    #VerticeFinal.append(arrayDi[j][2]) 
    j +=1
    if arrayDi[tam][2]==arrayDi[j][2]:
      auj =int(arrayDi[j][2])
      VerticeFinal.append(auj)
     # VerticeFinal.append(arrayDi[j][2])
  
  return VerticeInicial,VerticeFinal
     



#Criando função que recebe o arrayDi e matrizAdjNula
# ta errado 
def setValoresMatriz(aDi,grade0):
  arrayDi =aDi
  grade=grade0
  k = 1 # não pode ser menor do que 1 ;k vai de 1 ate o tamanhho do elemento
  l =0
  tamanho =int(NumeroDeNo(arrayDi))
  
  print(tamanho)
  while k < tamanho: #verifica a condição   
    while l <2:
      if arrayDi[k][l]== arrayDi[k][0]:
        auxk=int(arrayDi[k][l])
      l += 1
    if arrayDi[k][l]==arrayDi[k][2]:
      auxl=(arrayDi[k][l])
      auxl=int(auxl)
      #aqui devo devo atribuir os idx para coloca 1 ou 0
      grade[auxk-1][auxl-1]=1 # colando em um so lado 
      #teste
      grade[auxl-1][auxk-1]=1 # colando no outro lado (opcional)  
    l=0
    k += 1 #o passo de "incremento"
  while l<2:
    if arrayDi[k][l]== arrayDi[k][0]:
      auxk=int(arrayDi[k][l])
    l+= 1
  if arrayDi[k][l]==arrayDi[k][2]:
    auxl=int(arrayDi[k][l])
    grade[auxk-1][auxl-1]=1
  return grade    






            
       



# criando função adjacente  com valoes nulo
def criarMatrizAdj(numeroVertice):
    tamanho=int(numeroVertice)
    grade =[]
    for _ in range(tamanho):
        sublista =[]
        for _ in range(tamanho):
            sublista.append(0)
        grade.append(sublista)
    return grade



    
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


#estuda modularização no pythhon
def NumeroDeNo(arraDii):
    return arraDii[0][0]
  


def ola(var):
    return var
    print("ola mundo")


def divisao(n1,n2):
    if n2>0:
        return n1/n2

def f(vaa):
    print("dentro da função f")
    print(vaa)

def dumb():
    return f

## principal
"""
divi=divisao(8,0)
print(divi)

if divi:
    print(divi)
else:
    print("kkskskskksksks")


vaa=dumb()
print(type(vaa))

matriz=[[0, 1, 0, 0, 0],
 [1, 0, 0, 0, 1],
 [0, 0, 0, 0, 1],
 [0, 0, 0, 0, 1],
 [1, 1, 1, 1, 0]]

pprint(matriz)

mm=[[9,2],
 [3,4]]

NumeroDeNo(mm)

"""