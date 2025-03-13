"""Implementa un programa que solicite al usuario que ingrese una lista de
 números. Luego, imprime la lista pero detén la impresión si encuentras un
 número negativo. Nota: utilice la sentencia break cuando haga falta."""

numeros = input("ingrese una lista de numeros")
lista = [int(ele) for ele in numeros.split()]
for ele in lista:
    if (ele<0):
        break
    print(ele)
