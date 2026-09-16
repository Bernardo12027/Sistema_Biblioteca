import sqlite3

DB_NOME = "biblioteca.db"


def conectar():
    """Abre e retorna uma conexão com o banco de dados."""
    return sqlite3.connect(DB_NOME)


def criar_tabela():
    """Cria a tabela de livros caso ela ainda não exista."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER,
            quantidade INTEGER NOT NULL DEFAULT 1,
            emprestados INTEGER NOT NULL DEFAULT 0
        )
    """)
    conexao.commit()
    conexao.close()
