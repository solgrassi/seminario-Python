"""Cree un programa que dada una lista de números imprima sólo los que son
 pares. Nota: utilice la sentencia continue donde haga falta."""

lista = [1, 2, 4, 6, 8, 10, 56, 76, 77]
for i in lista: 
    if (int(i) % 2 != 0):
        continue
    print(i)
