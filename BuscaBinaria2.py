# Implemente uma função que receba:

# uma lista ordenada

# um número alvo

# Retorne:

# o índice do número, se existir

# - 1 se não existir

def BuscaBinaria():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # lista ordenada
    alvo = 9
    inicio = 0                   # Ponteiro para o começo da lista
    fim = len(numeros) - 1       # Ponteiro para o último índice da lista
    while inicio <= fim:
       meio = (inicio + fim) // 2 # Calculamos o índice do meio usando divisão inteira (//)
       chute = numeros[meio] # Pegamos o valor que está exatamente no meio da lista
       if chute == alvo:
           return meio # meio representa o índice
       elif chute < alvo:
            # Se o chute foi baixo, o alvo só pode estar na metade da DIREITA.
        inicio = meio + 1 # movemos o 'inicio' para logo após o meio atual.
       else:
          # Se o chute foi alto, o alvo só pode estar na metade da ESQUERDA.
          fim = meio - 1  # trazemos o 'fim' para logo antes do meio atual.
    return -1

print(BuscaBinaria())


       

       

       


   


