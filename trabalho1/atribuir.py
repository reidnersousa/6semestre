k = 1 # não pode ser menor do que 1 ;k vai de 1 ate o tamanhho do elemento
l =0
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