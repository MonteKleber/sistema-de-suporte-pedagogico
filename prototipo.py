from datetime import datetime

def aceitar_solicitacao(solicitacao): #define uma função para aceitar a solicitação
    if solicitacao ["status"] == "AGUARDANDO":
        solicitacao ["status"] = "EM ATENDIMENTO"
        solicitacao ["horario_de_atendimento"] = datetime.now().strftime("%H:%M:%S")
    else:
        print ("Não é possível aceitar essa solicitação")
        print (f"Status da solicitação: {solicitacao['status']}")

def concluir_solicitacao(solicitacao):#define uma função para concluir a solicitação
    if solicitacao ["status"] == "EM ATENDIMENTO":
        solicitacao ["status"] = "CONCLUÍDO"
        solicitacao ["horario_de_conclusao"] = datetime.now().strftime("%H:%M:%S")
    else:
        print ("Não é possível concluir essa solicitação")
        print (f"Status da solicitação:{solicitacao['status']}")

def exibir_solicitacao (solicitacao): #define uma função apenas para exibir a solicitação
    print ("=== SOLICITAÇÃO ===")
    print ("ID da solicitação")
    print (solicitacao["id"])
    print ("Problema:")
    print (solicitacao ["problema"])
    print ("Horário de abertura:")
    print (solicitacao ["horario_de_abertura"])
    print ("Horário de atendimento:")
    print (solicitacao ["horario_de_atendimento"])
    print ("Horário de conclusão:")
    print (solicitacao ["horario_de_conclusao"])
    print ("Status da demanda:")
    print (solicitacao ["status"])

def criar_solicitacao(id, alocacao, problema): #define uma função para criar solicitações
    horario_de_abertura = datetime.now().strftime ("%H:%M:%S")
    horario_de_atendimento = None
    horario_de_conclusao = None
    status = "AGUARDANDO"
    nova_solicitacao = {
        "id" : id,
        "alocacao" : alocacao,
        "problema" : problema,
        "horario_de_abertura" : horario_de_abertura,
        "horario_de_atendimento" : horario_de_atendimento,
        "horario_de_conclusao" : horario_de_conclusao,
        "status" : status,
    }
    return nova_solicitacao

professor = {
    "id": 1,
    "nome": "Carlos Bonfim"
}

turma = {
    "id": 1,
    "curso":"enfermagem",
    "codigo_turma": "ENF221N",
    "turno": "noturno"  
}

disciplina = {
    "id" : 1,
    "nome" : "Anatomia"
}

sala = {
    "id" : 1,
    "identificacao" : "Sala 207"
}

alocacao = {
    "id" : 1,
    "professor": professor,
    "turma": turma,
    "disciplina": disciplina,
    "sala": sala,
    "data_inicio": "26/08/2026",
    "data_fim": "10/09/2026"
}
while True:
    try:
        opcao = int(input("Informe o problema 1.Ar-Condicionado | 2.Projetor | 3.Material\n"))
        if opcao == 1 or opcao== 2 or opcao == 3:
            break
        else:
            print("Opção inválida")
    except ValueError:
        print ("DIGITE APENAS NÚMEROS!")
        continue
    
if opcao == 1:
    problema = "Ar-condicionado"
elif opcao == 2:
    problema = "Projetor"
elif opcao == 3:
    problema = "Material"

solicitacao = criar_solicitacao(1, alocacao, problema)
aceitar_solicitacao(solicitacao)
exibir_solicitacao(solicitacao)