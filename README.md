# Sistema de Biblioteca

Sistema de linha de comando (CLI) para gerenciar o acervo de uma biblioteca, com cadastro, busca, empréstimo e devolução de livros. Os dados são armazenados em um banco de dados SQLite.

## Funcionalidades

- Adicionar livro (título, autor, ano, quantidade de exemplares)
- Listar todos os livros cadastrados
- Buscar livro por título ou autor
- Atualizar dados de um livro existente
- Remover livro
- Registrar empréstimo de exemplar
- Registrar devolução de exemplar

## Estrutura do projeto

```
biblioteca/
├── database.py   # Conexão com o banco e criação da tabela
├── livro.py       # Funções de CRUD e empréstimo/devolução
├── main.py        # Menu interativo (ponto de entrada)
└── README.md
```


## Exemplo de uso

```
=== Sistema de Biblioteca ===
1. Adicionar livro
2. Listar livros
3. Buscar livro
4. Atualizar livro
5. Remover livro
6. Emprestar livro
7. Devolver livro
0. Sair
```

