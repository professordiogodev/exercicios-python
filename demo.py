
nomes = ["Adriana", "João", "Dr Flávio", "Guilhermina", "Celso", "Mariana", "Maria"]

# Imprimir todos os Elementos
for nome in nomes:
    print(nome)

# Imprimir números até N - 1
for numero in range(10):
    print(numero)

# Imprimir números de A a N - 1
for numero in range(5, 10):
    print(numero)


# Imprimir todas as letras (strings - texto - são elementos iteráveis)
nome = "diogo"
for letra in nome:
    print(letra)


# Nested For Loop - Imprimir todas as letras de todos os elementos
for nome in nomes:
    for letra in nome:
        print(letra)
