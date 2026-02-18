# Dada uma lista de IDs de usuários, use um set ou dict para encontrar se existe algum ID duplicado em $O(n)$ 

def tem_duplicatas(ids):
    vistos = set()  # Criar set vazio (deve usar set(), não {})  
    for n in ids:
        if n in vistos:
            return True
        vistos.add(n) #  Adiciona elemento 
    else: 
        return False

ids_do_banco = [1, 2, 3, 4]
print(tem_duplicatas(ids_do_banco))