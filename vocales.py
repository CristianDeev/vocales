def contar_vocales(frase):
    # Definimos las vocales y creamos un arreglo para almacenarlas
    vocales = 'aeiouAEIOU'
    vocales_encontradas = []
    
    # Contamos las vocales en la frase
    for letra in frase:
        if letra in vocales:
            vocales_encontradas.append(letra.lower())  # Agregamos la vocal en minúscula para evitar duplicados

    # Eliminamos duplicados de las vocales encontradas y mostramos los resultados
    vocales_unicas = list(set(vocales_encontradas))
    print(f"Vocales encontradas en la frase: {vocales_unicas}")
    print(f"Cantidad total de vocales: {len(vocales_encontradas)}")

# Solicitamos una frase al usuario y ejecutamos la función
frase = input("Ingresa una frase: ")
contar_vocales(frase)
