from database import criar_tabela
from livro import (
    adicionar_livro,
    listar_livros,
    buscar_livro,
    atualizar_livro,
    deletar_livro,
    emprestar_livro,
    devolver_livro,
)


def exibir_menu():
    print("\n=== Sistema de Biblioteca ===")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Buscar livro")
    print("4. Atualizar livro")
    print("5. Remover livro")
    print("6. Emprestar livro")
    print("7. Devolver livro")
    print("0. Sair")


def exibir_livros(livros):
    if not livros:
        print("Nenhum livro encontrado.")
        return

    print(f"\n{'ID':<4}{'Título':<30}{'Autor':<20}{'Ano':<6}{'Qtd':<5}{'Emprestados':<12}")
    print("-" * 80)
    for livro in livros:
        id_livro, titulo, autor, ano, quantidade, emprestados = livro
        ano_exibido = ano if ano else "-"
        print(f"{id_livro:<4}{titulo:<30}{autor:<20}{ano_exibido:<6}{quantidade:<5}{emprestados:<12}")


def main():
    criar_tabela()

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            ano = input("Ano de publicação (opcional): ").strip()
            quantidade = input("Quantidade de exemplares: ").strip()

            ano = int(ano) if ano.isdigit() else None
            quantidade = int(quantidade) if quantidade.isdigit() else 1

            adicionar_livro(titulo, autor, ano, quantidade)
            print("Livro adicionado com sucesso!")

        elif opcao == "2":
            exibir_livros(listar_livros())

        elif opcao == "3":
            termo = input("Digite o título ou autor para buscar: ").strip()
            exibir_livros(buscar_livro(termo))

        elif opcao == "4":
            id_livro = input("ID do livro a atualizar: ").strip()
            if not id_livro.isdigit():
                print("ID inválido.")
                continue

            print("Deixe em branco os campos que não quer alterar.")
            titulo = input("Novo título: ").strip() or None
            autor = input("Novo autor: ").strip() or None
            ano = input("Novo ano: ").strip()
            quantidade = input("Nova quantidade: ").strip()

            ano = int(ano) if ano.isdigit() else None
            quantidade = int(quantidade) if quantidade.isdigit() else None

            sucesso = atualizar_livro(int(id_livro), titulo, autor, ano, quantidade)
            print("Livro atualizado!" if sucesso else "Não foi possível atualizar (verifique o ID).")

        elif opcao == "5":
            id_livro = input("ID do livro a remover: ").strip()
            if not id_livro.isdigit():
                print("ID inválido.")
                continue

            sucesso = deletar_livro(int(id_livro))
            print("Livro removido!" if sucesso else "Livro não encontrado.")

        elif opcao == "6":
            id_livro = input("ID do livro para emprestar: ").strip()
            if not id_livro.isdigit():
                print("ID inválido.")
                continue

            _, mensagem = emprestar_livro(int(id_livro))
            print(mensagem)

        elif opcao == "7":
            id_livro = input("ID do livro para devolver: ").strip()
            if not id_livro.isdigit():
                print("ID inválido.")
                continue

            _, mensagem = devolver_livro(int(id_livro))
            print(mensagem)

        elif opcao == "0":
            print("Até mais!")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
