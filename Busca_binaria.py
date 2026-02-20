# Implemente uma função que encontre o índice de um elemento em uma lista ordenada de 1 milhão de itens. Meça o tempo comparando com uma busca linear comum.

import time # Importa a biblioteca para medir o tempo de execução

# Criamos uma lista de 0 a 999.999. No Back-End, isso simula uma coluna indexada de um DB.
lista_gigante = list(range(1000000))

# Definimos o alvo como o último elemento para forçar o "pior cenário" da busca linear.
alvo = 999999 

# --- BUSCA LINEAR ---
inicio_linear = time.time()  # Marca o timestamp de início

# Percorremos a lista um por um, do índice 0 até o final.
for i in range(len(lista_gigante)):
    # Se o valor no índice atual for o que buscamos...
    if lista_gigante[i] == alvo:
        break  # Interrompemos o loop (encontramos o alvo)

fim_linear = time.time()  # Marca o timestamp de término
# Exibe a diferença entre fim e início (Tempo total)
print(f"Tempo Linear: {fim_linear - inicio_linear} segundos")


# --- BUSCA BINÁRIA ---
inicio_binario = time.time()  # Marca o timestamp de início

inicio = 0                   # Ponteiro para o começo da lista
fim = len(lista_gigante) - 1 # Ponteiro para o último índice da lista

# Enquanto a área de busca não se fechar (início ultrapassar o fim)...
while inicio <= fim:
    # Calculamos o índice do meio usando divisão inteira (//)
    meio = (inicio + fim) // 2
    
    # Pegamos o valor que está exatamente no meio da lista
    chute = lista_gigante[meio]

    if chute == alvo:
        break  # Sucesso! Encontramos o alvo e saímos do loop
    
    elif chute < alvo:
        # Se o chute foi baixo, o alvo só pode estar na metade da DIREITA.
        # Então, movemos o 'inicio' para logo após o meio atual.
        inicio = meio + 1
    else:
        # Se o chute foi alto, o alvo só pode estar na metade da ESQUERDA.
        # Então, trazemos o 'fim' para logo antes do meio atual.
        fim = meio - 1

fim_binario = time.time()  # Marca o timestamp de término
# Exibe o tempo da busca binária (usando notação científica se for muito rápido)
print(f"Tempo Binário: {fim_binario - inicio_binario} segundos")

