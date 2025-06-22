import os

# Caminho do arquivo
ARQUIVO = "agenda.txt"

# Função para adicionar um contato
def adicionar_contato():
    nome = input("Digite o nome do contato:").strip()
    telefone = input("Infome o telefone: ").strip()
    if nome == "" or telefone == "":
        print("Nome e telefone não podem ser vazios")
        return
    with open(ARQUIVO,"a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {nome} | Telefone :{telefone}\n")
        print("Contato salvo!")

# Função para ler os contatos da agenda
def listar_contatos():
    if not os.path.exists(ARQUIVO):
        print("Não existe contatos salvos na agenda")
        return
    print("\n::::::::::LISTA DE CONTATOS::::::::::::::")
    with open(ARQUIVO,"r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        if not linhas:
            print("Agenda vazia")
        else:
            for linha in linhas:
                print(linha.strip())
#Função para bustar os contatos na agenda
def buscar_contato():
    termo = input("Digite o nome ou parte do nome: ")
    if not os.path.exists(ARQUIVO):
        print("Arquivo não encontrado")
        return    
    encontrado = False
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if termo in linha.lower():
                print("Encontrado:", linha.strip())
                encontrado = True
    if not encontrado:
        print("Nenhum contato encontrado com esse nome.")

#função para excluir contatos da agenda
def excluir_contato():
    nome = input("Digite o nome a excluir: ").strip().lower()
    if not os.path.exists(ARQUIVO):
        print("Arquivo não encontrado.")
        return
    nova_lista = []
    removido = False
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if nome not in linha.lower():
                nova_lista.append(linha)
            else:
                removido = True
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(nova_lista)
    if removido:
        print("Contato(s) excluído(s) com sucesso.")
    else:
        print("Nenhum contato com esse nome foi encontrado.")

# Função do menu principal
def menu():
    print("\n📒 === MENU DA AGENDA ===")
    print("[1] Adicionar contato")
    print("[2] Listar contatos")
    print("[3] Buscar contato")
    print("[4] Excluir contato")
    print("[5] Sair")
    return input("Escolha uma opção: ")       
#Programa pricipal
while True:
    opcao = menu()
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        buscar_contato()
    elif opcao == "4":
        excluir_contato()
    elif opcao == "5":
        print("Encerrando a agenda. Até logo !")
        break
    else:
        print("Opção inválida, tente novamente")