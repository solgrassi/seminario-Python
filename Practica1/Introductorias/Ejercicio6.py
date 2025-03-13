"""Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas
 listas, una con los número pares y otras con los que son impares. Imprima
 las listas al terminar de procesarlas.""" 

lista = [15, 2, 7, 68, 8, 10, 56, 76, 77]
pares = []
impares = []
for i in lista: 
    if ( i % 2 != 0):
        impares.append(i)
    else:
        pares.append(i)
print("lista pares: ", pares, "\nlista impares: ", impares)
