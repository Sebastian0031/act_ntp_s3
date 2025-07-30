frase = "programacion es divertida"
vocales = "aeiouAEIOU"
contador = 0
for letra in frase:
    if letra in vocales:
        contador += 1
print("Cantidad de vocales:", contador)
