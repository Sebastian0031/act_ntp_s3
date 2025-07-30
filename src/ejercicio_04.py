suma = 0
numero = int(input("ingresa un numero (0 para terminar): "))

while numero !=0:
    suma += numero
    numero = int(input("Ingresa otro numero (0 para terminar):"))

print("la suma total es:", suma)