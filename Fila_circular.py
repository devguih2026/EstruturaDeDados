# Imagine um buffer de log que armazena apenas as últimas 5 mensagens. Quando chegar a 6ª, a 1ª deve ser descartada

logs = []

def adicionar_log(lista_logs, msg):
    # Passo 1: Se estiver cheio, removemos o mais antigo
    if len(lista_logs) == 5:
        lista_logs.pop(0) 
    
    # Passo 2: Agora que garantimos que há espaço (ou já havia), adicionamos
    lista_logs.append(msg)
    
    return lista_logs

# Teste manual
adicionar_log(logs, "Msg 1")
adicionar_log(logs, "Msg 2")
adicionar_log(logs, "Msg 3")
adicionar_log(logs, "Msg 4")
adicionar_log(logs, "Msg 5")

# Adicionando a 6ª mensagem (remove a "Msg 1")
print(adicionar_log(logs, "Msg 6"))



