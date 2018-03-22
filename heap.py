#!/usr/bin/python3.5
import sys
def heapMax (lista, tam, i):
    maior = i # Initialize largest as root
    EE = 2 * i + 1    # left = 2*i + 1
    ED = 2 * i + 2    # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if EE < tam and lista[i] < lista[EE]:
        maior = EE

    # See if right child of root exists and is
    # greater than root
    if ED < tam and lista[maior] < lista[ED]:
        maior = ED

    # Change root, if needed
    if maior != i:
        lista[i],lista[maior] = lista[maior],lista[i] # swap

        # Heapify the root.
        heapMax(lista, tam, maior)

# The main function to sort an array of given size
def heapSort(lista):
    tam = len(lista)

    # Build a maxheap.
    for i in range(tam, -1, -1):
        heapMax(lista, tam, i)
    print("ARRAY :: ",lista)
    # One by one extract elements
    for i in range(tam-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i] # swap
        heapMax(lista, i, 0)

# Driver code to test above
#lista = [ 12, 11, 13, 5, 6, 7]
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
heapSort(lista)

tam = len(lista)
print ("O array eh")

print(lista)
#for i in range(n):
    #print ("%d" %arr[i])
