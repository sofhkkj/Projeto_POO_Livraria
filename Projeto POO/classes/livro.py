from db.conexao import conectar

class Livro:  #Classes e Objetos — definição da estrutura da entidade Livro
    def __init__(self, titulo, autor, ano_publicacao, editora, genero, isbn):
        # ✔️ 1. Atributos — definem as características do objeto Livro
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.editora = editora
        self.genero = genero
        self.isbn = isbn

    def salvar(self):  #Método — comportamento da classe Livro
        conexao = conectar()
        cursor = conexao.cursor()

        # Método com lógica de persistência no banco de dados
        sql = """
            INSERT INTO tb_livro (titulo, autor, editora, ano_publicacao, genero, isbn)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (
            self.titulo, self.autor, self.editora,
            self.ano_publicacao, self.genero, self.isbn
        )

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f"Livro '{self.titulo}' salvo com sucesso!")  #Confirmação de execução do método
