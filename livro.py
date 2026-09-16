from database import conectar


def adicionar_livro(titulo, autor, ano, quantidade):
    """Insere um novo livro no banco de dados."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO livros (titulo, autor, ano, quantidade) VALUES (?, ?, ?, ?)",
        (titulo, autor, ano, quantidade)
    )
    conexao.commit()
    conexao.close()


def listar_livros():
    """Retorna todos os livros cadastrados, ordenados por título."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros ORDER BY titulo")
    livros = cursor.fetchall()
    conexao.close()
    return livros


def buscar_livro(termo):
    """Busca livros pelo título ou autor (busca parcial)."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT * FROM livros WHERE titulo LIKE ? OR autor LIKE ?",
        (f"%{termo}%", f"%{termo}%")
    )
    resultados = cursor.fetchall()
    conexao.close()
    return resultados


def atualizar_livro(id_livro, titulo=None, autor=None, ano=None, quantidade=None):
    """Atualiza apenas os campos informados de um livro existente."""
    conexao = conectar()
    cursor = conexao.cursor()

    campos = []
    valores = []

    if titulo is not None:
        campos.append("titulo = ?")
        valores.append(titulo)
    if autor is not None:
        campos.append("autor = ?")
        valores.append(autor)
    if ano is not None:
        campos.append("ano = ?")
        valores.append(ano)
    if quantidade is not None:
        campos.append("quantidade = ?")
        valores.append(quantidade)

    if not campos:
        conexao.close()
        return False

    valores.append(id_livro)
    query = f"UPDATE livros SET {', '.join(campos)} WHERE id = ?"
    cursor.execute(query, valores)
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    conexao.close()
    return linhas_afetadas > 0


def deletar_livro(id_livro):
    """Remove um livro pelo ID."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    conexao.close()
    return linhas_afetadas > 0


def emprestar_livro(id_livro):
    """Registra o empréstimo de um exemplar, se houver disponibilidade."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT quantidade, emprestados FROM livros WHERE id = ?", (id_livro,))
    resultado = cursor.fetchone()

    if resultado is None:
        conexao.close()
        return False, "Livro não encontrado."

    quantidade, emprestados = resultado
    if emprestados >= quantidade:
        conexao.close()
        return False, "Não há exemplares disponíveis para empréstimo."

    cursor.execute("UPDATE livros SET emprestados = emprestados + 1 WHERE id = ?", (id_livro,))
    conexao.commit()
    conexao.close()
    return True, "Empréstimo realizado com sucesso."


def devolver_livro(id_livro):
    """Registra a devolução de um exemplar emprestado."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT emprestados FROM livros WHERE id = ?", (id_livro,))
    resultado = cursor.fetchone()

    if resultado is None:
        conexao.close()
        return False, "Livro não encontrado."

    emprestados = resultado[0]
    if emprestados <= 0:
        conexao.close()
        return False, "Não há exemplares emprestados deste livro."

    cursor.execute("UPDATE livros SET emprestados = emprestados - 1 WHERE id = ?", (id_livro,))
    conexao.commit()
    conexao.close()
    return True, "Devolução registrada com sucesso."
