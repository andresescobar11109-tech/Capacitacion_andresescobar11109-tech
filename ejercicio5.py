# EJERCICIO 5: CONTADOR DE VOCALES
frase = input()
vocal = []
frase_limpia = frase.replace(" ", "").lower()

for i in (frase_limpia):
    if (i == "a"):
        vocal.append(i)
    if (i == "e"):
        vocal.append(i)
    if (i == "i"):
        vocal.append(i)
    if (i == "o"):
        vocal.append(i)
    if (i == "u"):
        vocal.append(i)
print("Total de vocales: %d" % len(vocal))
