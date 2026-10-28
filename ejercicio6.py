# EJERCICIO 6: Inversor de arreglos.
# arreglo = [10, 20, 30, 40]
arreglo = [int(x)
           for x in input("Escribe números separados por espacio: ").split()]
a = 0
arreglo_final = []

for i in arreglo:
    a -= 1
    i = 0 + a
    arreglo_final.append(arreglo[i])
print(arreglo_final)
