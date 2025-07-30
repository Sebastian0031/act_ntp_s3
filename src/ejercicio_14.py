import random
secreto = random.randint(1, 10)
adivinanza = int(input("Adivina el número (entre 1 y 10): "))
while adivinanza != secreto:
    adivinanza = int(input("Incorrecto. Intenta de nuevo: "))
print("¡Felicidades! Adivinaste el número.")