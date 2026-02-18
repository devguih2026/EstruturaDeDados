# Crie uma função que inverta uma string sem usar [::-1]. Use uma Pilha.

def InverterString(a):
   stack: list[str] = [] # stack significa pilha (estrutura LIFO – Last In, First Out)
   for char in a:  # Percorre cada caractere da string a
      stack.append(char) # Adiciona cada caractere na pilha (stack).
   resultado = "" # variável vazia para armazenar a string invertida
   while len(stack) > 0: # Enquanto a pilha não estiver vazia...
        resultado += stack.pop() # stack.pop() remove e retorna o último elemento da lista
   print(resultado) 

InverterString("Python")



    

