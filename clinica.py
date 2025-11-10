# Lista para armazenar os dados em memória
pacientes = []
medicos = []
agendamentos = []

# --- Funções do Passo 2 (Pacientes e Estatísticas) ---

def cadastrar_paciente():
    """Cadastra um novo paciente, agora incluindo o CPF."""
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome do paciente: ")
    cpf = input("CPF (XXX.XXX.XXX-XX): ")
    
    while True:
        try:
            idade = int(input("Idade: "))
            if idade <= 0:
                print("Por favor, insira uma idade válida.")
                continue
            break
        except ValueError:
            print("Erro: A idade deve ser um número.")
            
    telefone = input("Telefone: ")
    
    paciente = {
        "id": len(pacientes) + 1,
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "telefone": telefone
    }
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def ver_estatisticas():
    """Calcula e exibe as estatísticas dos pacientes."""
    if not pacientes:
        print("\nNenhum paciente cadastrado.")
        return

    total_pacientes = len(pacientes)
    idades = [p["idade"] for p in pacientes]
    idade_media = sum(idades) / total_pacientes
    paciente_mais_novo = min(pacientes, key=lambda p: p["idade"])
    paciente_mais_velho = max(pacientes, key=lambda p: p["idade"])
    
    print("\n--- Estatísticas da Clínica ---")
    print(f"Número total de pacientes: {total_pacientes}")
    print(f"Idade média dos pacientes: {idade_media:.1f} anos")
    print(f"Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")

def buscar_paciente():
    """Busca um paciente pelo nome e exibe seus dados, incluindo CPF."""
    if not pacientes:
        print("\nNenhum paciente cadastrado.")
        return
    
    nome_busca = input("\nDigite o nome para buscar: ").lower()
    encontrados = [p for p in pacientes if nome_busca in p["nome"].lower()]
    
    if encontrados:
        print(f"\n--- Pacientes Encontrados ---")
        for p in encontrados:
            
            print(f"ID: {p['id']} | Nome: {p['nome']} | CPF: {p['cpf']} | Idade: {p['idade']} | Tel: {p['telefone']}")
    else:
        print("Nenhum paciente encontrado.")

def listar_todos_pacientes():
    """Exibe todos os pacientes cadastrados, incluindo CPF."""
    if not pacientes:
        print("\nNenhum paciente cadastrado.")
        return
        
    print("\n--- Lista de Todos os Pacientes ---")
    for p in pacientes:
        print(f"ID: {p['id']} | Nome: {p['nome']} | CPF: {p['cpf']} | Idade: {p['idade']} | Tel: {p['telefone']}")

# --- Funções Adicionais (Contexto Geral / Passo 5) ---

def cadastrar_medico():
    """Cadastra um novo médico."""
    print("\n--- Cadastro de Médico ---")
    nome = input("Nome do médico: ")
    especialidade = input("Especialidade: ")
    medico = {
        "id": len(medicos) + 1,
        "nome": nome,
        "especialidade": especialidade
    }
    medicos.append(medico)
    print("Médico cadastrado com sucesso!")

def listar_medicos():
    """Lista todos os médicos cadastrados."""
    if not medicos:
        print("\nNenhum médico cadastrado.")
        return
    print("\n--- Lista de Médicos ---")
    for m in medicos:
        print(f"ID: {m['id']} | Nome: {m['nome']} | Especialidade: {m['especialidade']}")

def agendar_consulta():
    """Agenda uma nova consulta vinculando paciente e médico."""
    print("\n--- Agendamento de Consulta ---")
    
    if not pacientes or not medicos:
        print("Erro: É preciso ter pacientes E médicos cadastrados para agendar.")
        return

    # Selecionar Paciente
    listar_todos_pacientes()
    try:
        id_paciente = int(input("Digite o ID do paciente: "))
        paciente_selecionado = next((p for p in pacientes if p['id'] == id_paciente), None)
        if not paciente_selecionado:
            print("ID do paciente não encontrado.")
            return
    except ValueError:
        print("ID inválido.")
        return

    # Selecionar Médico
    listar_medicos()
    try:
        id_medico = int(input("Digite o ID do médico: "))
        medico_selecionado = next((m for m in medicos if m['id'] == id_medico), None)
        if not medico_selecionado:
            print("ID do médico não encontrado.")
            return
    except ValueError:
        print("ID inválido.")
        return

    data = input("Digite a data da consulta (DD/MM/AAAA): ")
    hora = input("Digite a hora da consulta (HH:MM): ")
    
    agendamento = {
        "id": len(agendamentos) + 1,
        "paciente": paciente_selecionado['nome'],
        "medico": medico_selecionado['nome'],
        "especialidade": medico_selecionado['especialidade'],
        "data": data,
        "hora": hora
    }
    agendamentos.append(agendamento)
    print("Agendamento realizado com sucesso!")

def listar_agendamentos():
    """Lista todos os agendamentos realizados."""
    if not agendamentos:
        print("\nNenhum agendamento.")
        return
    print("\n--- Lista de Agendamentos ---")
    for a in agendamentos:
        print(f"ID: {a['id']} | Data: {a['data']} | Hora: {a['hora']} | Paciente: {a['paciente']} | Médico: {a['medico']} ({a['especialidade']})")

# --- Menu Principal ---

def main():
    """Função principal que exibe o menu e gerencia o loop."""
    while True:
        print("\n=== SISTEMA CLÍNICA VIDA+ (Completo) ===")
        print("--- Pacientes ---")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas dos pacientes")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("--- Médicos e Agendamentos ---")
        print("5. Cadastrar médico")
        print("6. Listar médicos")
        print("7. Agendar consulta")
        print("8. Listar agendamentos")
        print("9. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            ver_estatisticas()
        elif opcao == '3':
            buscar_paciente()
        elif opcao == '4':
            listar_todos_pacientes()
        elif opcao == '5':
            cadastrar_medico()
        elif opcao == '6':
            listar_medicos()
        elif opcao == '7':
            agendar_consulta()
        elif opcao == '8':
            listar_agendamentos()
        elif opcao == '9':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()