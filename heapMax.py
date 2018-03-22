#!/usr/bin/python3.5
#PARA RODAR O PROGRAMA  ./heapMax.py ArquivoDeEntrada.in
#PARA RODAR O PROGRAMA VENDO OS PASSOS ./heapMax.py ArquivoDeEntrada.in | more
import sys

def heapMax(lista, i):
    EE = 2*i
    ED = (2*i)+1

    print("INDEX DE I : ", i)
    print("INDEX DE EE : ",EE)
    print("INDEX DE ED : ",ED)
    if EE <= len(lista)-1 and lista[EE] > lista[i]:
        maior = EE
        print("EE maior ", lista[EE])
    else:
        maior = i
        print("i maior ", lista[i])

    if ED <= len(lista)-1 and lista[ED] > lista[maior]:
        maior = ED
        print("ED maior", lista[ED])

    if maior != i:
        aux = lista[i]
        lista[i] = lista[maior]
        lista[maior] = aux
        print("ELEMENTO MAIOR :::: ", lista[i])
        print('\033[31m',lista,'\033[0;0m')
        heapMax(lista, maior)

#lista = [1,3,4,2,5,8,6]
#lista = [0,1,2,3,4,5,6,7,9,-1]
#print('\033[31m',lista,'\033[0;0m')
lista = []
nome = sys.argv[1]
arq = open(nome, 'r')
i = 0
lista.append(0)
for line in arq:
    convertido = int(line)
    lista.append(convertido)
    i = i + 1
arq.close()


for i in range(int(len(lista)/2),0,-1):
    print("i",i)
    heapMax(lista, i)

print('\033[31m',lista,'\033[0;0m')