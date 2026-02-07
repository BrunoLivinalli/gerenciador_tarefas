import json
import os

ARQUIVO_TAREFAS = "tarefas.json"


def carregar_tarefas():
    # Carrega tarefas do arquivo JSON
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []

    with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_tarefas(tarefas):
    # Salva a lista de tarefas no arquivo JSON.
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ").strip()

    if not descricao: # usuario não digitou nada
        print("A tarefa não pode ser vazia")
        return

    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

    print("Tarefa adicionada com sucesso!")


def listar_tarefas(tarefas):
    if not tarefas: # Lista Vazia
        print(" Nenhuma tarefa cadastrada.")
        return

    print("\n Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "CONCLUIDA" if tarefa["concluida"] else "X"
        print(f"{i}. {tarefa['descricao']} - {status}")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        indice = int(input("Número da tarefa a marcar como concluída: "))
        tarefas[indice - 1]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa marcada como concluída!")
    except (ValueError, IndexError):
        print("Opção inválida!")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        indice = int(input("Número da tarefa a remover: "))
        tarefa_removida = tarefas.pop(indice - 1)
        salvar_tarefas(tarefas)
        print(f"🗑️ Tarefa removida: {tarefa_removida['descricao']}")
    except (ValueError, IndexError):
        print("Opção inválida!")


def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\n-> GERENCIADOR DE TAREFAS")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Saindo")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
