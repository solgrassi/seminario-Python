"""Haz un programa que pida al usuario que ingrese una temperatura en
 grados Celsius y luego convierta esa temperatura a grados Fahrenheit,
 mostrando el resultado"""

temp = int(input("ingrese una temperatura en grados Celsius"))
temp = temp * 1.8 + 32
print(f"La temperatura ingresada corresponde a: {temp:.1f} °F")