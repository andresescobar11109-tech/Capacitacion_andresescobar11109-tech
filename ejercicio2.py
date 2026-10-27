frase = "Anita lava la tina"

frase_limpia = frase.replace(" ", "").lower()

if frase_limpia == frase_limpia[::-1]:
    print("Es palíndromo")
else:
    print("No es palíndromo")
