# Refaça o exercício anterior, mas usando recursão.

# Pense:

# Qual é o caso base?

# Como você reduz o problema a cada chamada?

def busca_binaria_recursiva(numeros, alvo, inicio, fim):
    
    # Caso base 1: intervalo inválido → não encontrou
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    
    # Caso base 2: encontrou o elemento
    if numeros[meio] == alvo:
        return meio
    
    # Se o alvo é menor, busca na metade esquerda
    elif alvo < numeros[meio]:
        return busca_binaria_recursiva(numeros, alvo, inicio, meio - 1)
    
    # Se o alvo é maior, busca na metade direita
    else:
        return busca_binaria_recursiva(numeros, alvo, meio + 1, fim)


# Exemplo de uso
numeros = [1,2,3,4,5,6,7,8,9,10]
print(busca_binaria_recursiva(numeros, 9, 0, len(numeros) - 1))