contador =0
palabra = input("Escribe una palabra ('fin'para terminar): ")

while palabra.lower() != "fin":
    contador += 1
    palabra = input("Escribe otra palabra ('fin' para terminar): ")
print("Se ingresaron", contador, "palabras.")