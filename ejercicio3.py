# Ejercicio 3: Bee Fight
avispas = int(input("Número de avispas: \n"))
abejas = int(input("Número de abejas: \n"))
puntos_avispas = avispas * 3
puntos_abejas = abejas * 2
if puntos_abejas > puntos_avispas:
    print(f"Ganan las Abejas ({puntos_abejas} vs {puntos_avispas})")
else:
    print(f"Ganan las Avispas ({puntos_avispas} vs {puntos_abejas})")
